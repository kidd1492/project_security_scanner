import os, sys
import main_menu, helper

def list_available_files(directory_name):
    print("#" * 42)
    print("reports")
    print("#" * 42, "\n\n")

    project_name = f"project_{directory_name.split(os.sep)[-1]}"
    base_path = os.path.join("scr", "projects", project_name)
    reports_dir = os.path.join(base_path, "reports")
    scans_dir = os.path.join(base_path, "scans")

    all_files = []

    for folder in [reports_dir, scans_dir]:
        if os.path.exists(folder):
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                if os.path.isfile(file_path):
                    all_files.append((file, file_path))
        else:
            print(f"Warning: Directory does not exist -> {folder}")

    # Add menu options
    all_files.append(("MAIN MENU", None))
    all_files.append(("EXIT", None))

    # Display menu
    for index, (filename, _) in enumerate(all_files, start=1):
        print(f"{index}. {filename}")

    print("\n")
    try:
        menu_selection = int(input("Enter Number for Option: "))
        selected_label, selected_path = all_files[menu_selection - 1]

        if selected_label == "EXIT":
            helper.clear_screen()
            sys.exit()
        elif selected_label == "MAIN MENU":
            helper.clear_screen()
            main_menu.create_menu("update")
        else:
            #helper.clear_screen()
            content = helper.read_file_content(selected_path)
            print(content)

            close = input("Press Enter key to close: ")
            if close == "":
                helper.clear_screen()
                list_available_files(directory_name)

    except (ValueError, IndexError):
        print("\nInvalid selection. Please try again.\n")