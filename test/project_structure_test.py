from src.project_structure import ProjectStructure


PROJECT = "test/benchmark_large"

analyzer = ProjectStructure(PROJECT)

project = analyzer.analyze()

for file_path, structure in project.items():

    print(f"\nFile: {file_path}")

    print("Functions:")
    for function in structure["functions"]:
        print(
            f"  {function['name']} "
            f"({function['start_line']}-{function['end_line']})"
        )

    print("Structs:")
    for struct in structure["structs"]:
        print(
            f"  {struct['name']} "
            f"({struct['start_line']}-{struct['end_line']})"
        )

        for field in struct["fields"]:
            print(
                f"    {field['type']} "
                f"{field['name']}"
            )

    print("Calls:")
    for call in structure["calls"]:
        print(
            f"  {call['name']} "
            f"(line {call['start_line']})"
        )