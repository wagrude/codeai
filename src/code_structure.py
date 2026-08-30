from src.ast_parser import CParser


class CodeStructure:

    def __init__(self):
        self.parser = CParser()

    def analyze(self, source_code):
        tree = self.parser.parse(source_code)

        structure = {
            "includes": [],
            "functions": [],
            "calls": [],
            "structs": []
        }

        self._walk(
            tree.root_node,
            structure,
            source_code
        )

        return structure

    def _walk(self, node, structure, source_code):

        if node.type == "preproc_include":
            structure["includes"].append({
                "content": self._text(node, source_code),
                "start_line": node.start_point[0] + 1,
                "end_line": node.end_point[0] + 1
            })

        elif node.type == "struct_specifier":
            name_node = node.child_by_field_name("name")

            if name_node is not None:
                fields = []

                body = node.child_by_field_name("body")

                if body is not None:
                    for field in body.named_children:

                        if field.type != "field_declaration":
                            continue

                        field_type = field.child_by_field_name("type")
                        field_name = field.child_by_field_name("declarator")

                        fields.append({
                            "type": (
                                self._text(
                                    field_type,
                                    source_code
                                )
                                if field_type is not None
                                else None
                            ),
                            "name": (
                                self._text(
                                    field_name,
                                    source_code
                                )
                                if field_name is not None
                                else None
                            )
                        })

                structure["structs"].append({
                    "name": self._text(
                        name_node,
                        source_code
                    ),
                    "fields": fields,
                    "start_line": node.start_point[0] + 1,
                    "end_line": node.end_point[0] + 1
                })

        elif node.type == "type_definition":
            type_node = node.child_by_field_name("type")
            name_node = node.child_by_field_name("declarator")

            if (
                type_node is not None
                and type_node.type == "struct_specifier"
                and name_node is not None
            ):
                body = type_node.child_by_field_name("body")

                fields = []

                if body is not None:
                    for field in body.named_children:

                        if field.type != "field_declaration":
                            continue

                        field_type = field.child_by_field_name("type")
                        field_declarator = field.child_by_field_name(
                            "declarator"
                        )

                        fields.append({
                            "type": (
                                self._text(
                                    field_type,
                                    source_code
                                )
                                if field_type is not None
                                else None
                            ),
                            "name": (
                                self._text(
                                    field_declarator,
                                    source_code
                                )
                                if field_declarator is not None
                                else None
                            )
                        })

                structure["structs"].append({
                    "name": self._text(
                        name_node,
                        source_code
                    ),
                    "fields": fields,
                    "start_line": node.start_point[0] + 1,
                    "end_line": node.end_point[0] + 1
                })

        elif node.type == "function_definition":
            function = self._extract_function(
                node,
                source_code
            )

            if function:
                structure["functions"].append(function)

        elif node.type == "call_expression":
            function_node = node.child_by_field_name(
                "function"
            )

            if function_node:
                structure["calls"].append({
                    "name": self._text(
                        function_node,
                        source_code
                    ),
                    "start_line": node.start_point[0] + 1,
                    "end_line": node.end_point[0] + 1
                })

        for child in node.children:
            self._walk(
                child,
                structure,
                source_code
            )

    def _extract_function(self, node, source_code):

        declarator = node.child_by_field_name(
            "declarator"
        )

        if declarator is None:
            return None

        name = self._find_function_name(
            declarator,
            source_code
        )

        if name is None:
            return None

        return_type_node = node.child_by_field_name(
            "type"
        )

        return_type = None

        if return_type_node is not None:
            return_type = self._text(
                return_type_node,
                source_code
            )

        function_declarator = self._find_function_declarator(
            declarator
        )

        parameters = []

        if function_declarator is not None:
            parameter_list = (
                function_declarator.child_by_field_name(
                    "parameters"
                )
            )

            if parameter_list is not None:
                parameters = self._extract_parameters(
                    parameter_list,
                    source_code
                )

        return {
            "name": name,
            "return_type": return_type,
            "parameters": parameters,
            "start_line": node.start_point[0] + 1,
            "end_line": node.end_point[0] + 1
        }

    def _find_function_name(self, node, source_code):

        current = node

        while current is not None:

            if current.type == "identifier":
                return self._text(
                    current,
                    source_code
                )

            current = current.child_by_field_name(
                "declarator"
            )

        return None

    def _find_function_declarator(self, node):

        current = node

        while current is not None:

            if current.type == "function_declarator":
                return current

            current = current.child_by_field_name(
                "declarator"
            )

        return None

    def _extract_parameters(self, parameter_list, source_code):

        parameters = []

        for child in parameter_list.named_children:

            if child.type != "parameter_declaration":
                continue

            parameter = {
                "type": None,
                "name": None
            }

            type_node = child.child_by_field_name(
                "type"
            )

            declarator = child.child_by_field_name(
                "declarator"
            )

            if type_node is not None:
                parameter["type"] = self._text(
                    type_node,
                    source_code
                )

            if declarator is not None:
                parameter["name"] = self._text(
                    declarator,
                    source_code
                )

            parameters.append(parameter)

        return parameters

    def _text(self, node, source_code):
        return source_code[
            node.start_byte:node.end_byte
        ]