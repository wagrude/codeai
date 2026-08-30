from src.scanner import scan_project
from src.code_structure import CodeStructure


class ProjectStructure:

    def __init__(self, project_path):
        self.project_path = project_path
        self.analyzer = CodeStructure()

    def analyze(self):
        project = {}

        files = scan_project(self.project_path)

        for file_path in files:
            with open(file_path, "r", encoding="utf-8") as file:
                source = file.read()

            project[file_path] = self.analyzer.analyze(source)

        return project