from tree_sitter import Language, Parser
import tree_sitter_c


class CParser:

    def __init__(self):
        self.parser = Parser(
            Language(tree_sitter_c.language())
        )

    def parse(self, source_code):
        tree = self.parser.parse(
            source_code.encode("utf-8")
        )

        return tree
