from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener


GENERATED_ROOT = Path(__file__).resolve().parents[1] / "generated"


class ParseError(Exception):
    pass


class _CollectingErrorListener(ErrorListener):
    def __init__(self) -> None:
        super().__init__()
        self.messages: list[str] = []

    def syntaxError(self, recognizer: Any, offendingSymbol: Any, line: int, column: int, msg: str, e: Any) -> None:
        self.messages.append(f"line {line}:{column} {msg}")


def parse(text: str, grammar: str, start_rule: str = "program") -> Any:
    grammar_dir = GENERATED_ROOT / grammar
    if not grammar_dir.exists():
        raise ParseError(f"Generated parser is missing: {grammar_dir}. Run python setup.py.")

    sys.path.insert(0, str(grammar_dir))
    try:
        if grammar == "recursive":
            from MPRecursiveLexer import MPRecursiveLexer
            from MPRecursiveParser import MPRecursiveParser
        elif grammar == "repeated":
            from MPRepeatedLexer import MPRepeatedLexer
            from MPRepeatedParser import MPRepeatedParser
        else:
            raise ValueError(f"Unknown grammar: {grammar}")

        input_stream = InputStream(text)
        lexer = MPRecursiveLexer(input_stream) if grammar == "recursive" else MPRepeatedLexer(input_stream)
        lexer_errors = _CollectingErrorListener()
        lexer.removeErrorListeners()
        lexer.addErrorListener(lexer_errors)
        tokens = CommonTokenStream(lexer)

        parser = MPRecursiveParser(tokens) if grammar == "recursive" else MPRepeatedParser(tokens)
        parser_errors = _CollectingErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(parser_errors)
        try:
            tree = getattr(parser, start_rule)()
        except AttributeError as error:
            raise ValueError(f"Unknown start rule: {start_rule}") from error

        errors = lexer_errors.messages + parser_errors.messages
        if errors:
            raise ParseError("; ".join(errors))
        return tree, parser
    finally:
        sys.path.remove(str(grammar_dir))
