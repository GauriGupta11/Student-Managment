from core.display import show_menu
from core.student_ops import handle_user_input

def main():
    while True:
        show_menu()
        should_continue = handle_user_input()
        if not should_continue:
            break

if __name__ == "__main__":
    main()
