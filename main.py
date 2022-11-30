import commands


def main():
    while True:
        command = input('Enter command:\n'
                        '1 - Create Index\n'
                        '2 - Delete Index\n'
                        '3 - View Indices\n'
                        '0 - Exit')

        match command:
            case '1':
                command = commands.Create()
            case '2':
                command = commands.Delete()
            case '3':
                command = commands.View()
            case '0':
                return
            case _:
                print('Command not found')
                continue

        command.run()


if __name__ == '__main__':
    main()
