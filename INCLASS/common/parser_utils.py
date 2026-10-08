from __future__ import annotations

import importlib
import sys
from pathlib import Path

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener


GENERATED_ROOT = Path(__file__).resolve().parents[1] / "generated"


class ParseError(Exception):
    pass


class _Errors(ErrorListener):
    def __init__(self) -> None:
        super().__init__()
        self.messages: list[str] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.messages.append(f"line {line}:{column} {msg}")


def parse(text: str, grammar: str, start_rule: str = "program"):
    folder = GENERATED_ROOT / grammar
    if not folder.exists():
        raise ParseError(f"Missing generated parser {folder}; run setup.py first")
    sys.path.insert(0, str(folder))
    try:
        lexer_module = importlib.import_module(f"{grammar}Lexer")
        parser_module = importlib.import_module(f"{grammar}Parser")
        lexer_class = getattr(lexer_module, f"{grammar}Lexer")
        parser_class = getattr(parser_module, f"{grammar}Parser")
        lexer = lexer_class(InputStream(text))
        lexer_errors = _Errors()
        lexer.removeErrorListeners()
        lexer.addErrorListener(lexer_errors)
        parser = parser_class(CommonTokenStream(lexer))
        parser_errors = _Errors()
        parser.removeErrorListeners()
        parser.addErrorListener(parser_errors)
        tree = getattr(parser, start_rule)()
        errors = lexer_errors.messages + parser_errors.messages
        if errors:
            raise ParseError("; ".join(errors))
        return tree
    finally:
        sys.path.remove(str(folder))
