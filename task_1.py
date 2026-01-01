from pathlib import Path
import shutil
import argparse


def recursive_folder_copy(source: Path, output: Path):
    try:
        for element in source.iterdir():
            if element.is_dir():
                recursive_folder_copy(element, output)
            else:
                try:
                    extension = element.suffix[1:]
                    if not extension:
                        folder_name = "no_extension"
                    else:
                        folder_name = extension

                    target_folder = output / folder_name
                    target_folder.mkdir(exist_ok=True, parents=True)
                    shutil.copy2(element, target_folder / element.name)
                except Exception as e:
                    print(f"[Помилка копіювання файлу] {element}: {e}")

    except PermissionError:
        print(f"[Помилка доступу] {source}")
    except FileNotFoundError:
        print(f"[Помилка] Директорію не знайдено: {source}")
    except Exception as e:
        print(f"[Загальна помилка] {e}")

def main():
    parser = argparse.ArgumentParser(description="Сортування файлів")
    parser.add_argument("source", nargs='?', help="Шлях до вихідної директорії")
    parser.add_argument("output", nargs="?", default="dist", help="Шлях до директорії призначення")
    args = parser.parse_args()
    source_str = args.source
    

    if not source_str:
        source_str = input("Введіть шлях до вихідної директорії: ").strip()
        
    source_path = Path(source_str)
    output_path = Path(args.output)

    if not source_path.exists() or not source_path.is_dir():
        print(f"Помилка: Директорія '{source_path}' не існує.")
        return

    print(f"Починаємо копіювання з '{source_path}' у '{output_path}'...")
    recursive_folder_copy(source_path, output_path)
    print("Готово!")

if __name__ == "__main__":
    main()
