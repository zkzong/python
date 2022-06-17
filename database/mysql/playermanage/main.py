import CRUD

option = 0

print("\n欢迎光临，请选择数据库操作！")

while option != 6:
    print("\n---------------------------")
    print("选择操作: \n"
          "0. 读取显示所有数据\n"
          "1. 创建数据库\n"
          "2. 插入新的数据\n"
          "3. 注册新球员\n"
          "4. 预约\n"
          "5. 删除所有的表\n"
          "6. 退出")
    print("---------------------------")

    option = int(input())

    if option == 0:

        CRUD.readAll()

    elif option == 1:

        CRUD.createDB()

    elif option == 2:

        CRUD.insertRows()

    elif option == 3:

        CRUD.insertRow(0)

    elif option == 4:

        print("\nConsultas: \n"
          "0. 查看目前的冠军球队?\n"
          "1. 游戏角色的比较?\n"
          "2. 玩家ID的特点?\n"
          "3. 其中最有特点的球员?\n"
          "4. 你感觉每个队最多的球员？\n"
          "5. 让所有的球员，他们的代表队屠杀和死亡\n"
          "6. 退出")
        readOpt = int(input())

        if readOpt == 0:
            CRUD.readTables(0)
        elif readOpt == 1:
            CRUD.readTables(1)
        elif readOpt == 2:
            CRUD.readTables(2)
        elif readOpt == 3:
            CRUD.readTables(3)
        elif readOpt == 4:
            CRUD.readTables(4)
        elif readOpt == 5:
            CRUD.readTables(5)

    elif option == 5:
         CRUD.deleteTables()

    elif option == 6:
        quit()


