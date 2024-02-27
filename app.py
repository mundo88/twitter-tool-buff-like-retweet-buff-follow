from menu.Menu import Menu

if __name__ == '__main__':
    menu = Menu()
    disconect = False
    while not disconect:
        menu.printMenu()
        option = input('Nhập lựa chọn: ')
        if option in menu.close:
            print('Đóng ứng dụng...')
            disconect = True
            break
        control = menu.control_option(option)
        
        