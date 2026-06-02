shop_name = ""
product_name = ""
description = ""
category = ""
keywords = []
discount_codes = []

while True:
    print("\n===== HE THONG QUAN LY SAN PHAM SHOPEE =====")
    print("1. Nhap du lieu san pham va xem bao cao")
    print("2. Chuan hoa ten shop")
    print("3. Kiem tra ma giam gia hop le")
    print("4. Tim kiem va thay the tu khoa")
    print("5. Thoat")

    choice = input("Nhap lua chon: ")

    if not choice.isdigit():
        print("Lua chon khong hop le")
        continue

    choice = int(choice)

    if choice == 1:
        shop_name = input("Nhap ten shop: ")

        if shop_name.strip() == "":
            print("Ten shop khong duoc bo trong")
            continue

        product_name = input("Nhap ten san pham: ")

        description = input("Nhap mo ta san pham: ")

        if description.strip() == "":
            print("Mo ta san pham khong duoc rong")
            continue

        category = input("Nhap danh muc san pham: ")

        keyword_input = input("Nhap danh sach tu khoa (cach nhau boi dau phay): ")

        keywords = keyword_input.split(",")

        for i in range(len(keywords)):
            keywords[i] = keywords[i].strip()

        print("\n===== BAO CAO THONG KE =====")
        print("Ten shop:", shop_name.strip())
        print("Ten san pham:", product_name.strip().title())
        print("Mo ta san pham:", description.strip())
        print("Do dai mo ta:", len(description.strip()))
        print("Danh muc:", category.strip().lower())
        print("Danh sach tu khoa:", keywords)
        print("So luong tu khoa:", len(keywords))
        print("Mo ta viet thuong:", description.strip().lower())
        print("Mo ta viet hoa:", description.strip().upper())

    elif choice == 2:
        if shop_name.strip() == "":
            print("Chua co ten shop")
        else:
            new_shop = shop_name.strip().lower()
            new_shop = new_shop.replace(" ", "-")

            if not new_shop.startswith("shop-"):
                new_shop = "shop-" + new_shop

            print("Ten shop ban dau:", shop_name)
            print("Ten shop sau chuan hoa:", new_shop)

    elif choice == 3:
        code = input("Nhap ma giam gia: ").strip()

        if code == "":
            print("Ma giam gia khong duoc rong")

        elif " " in code:
            print("Ma giam gia khong duoc chua khoang trang")

        elif len(code) < 6 or len(code) > 12:
            print("Ma giam gia phai tu 6 den 12 ky tu")

        elif code != code.upper():
            print("Ma giam gia phai viet hoa toan bo")

        elif not code.isalnum():
            print("Ma giam gia chi duoc chua chu cai va chu so")

        elif not code.startswith("SALE"):
            print("Ma giam gia phai bat dau bang SALE")

        else:
            discount_codes.append(code)
            print("Ma giam gia hop le")
            print("Danh sach ma giam gia hien tai:")
            print(discount_codes)

    elif choice == 4:
        if description.strip() == "":
            print("Chua co mo ta san pham")
        else:
            old_word = input("Nhap tu khoa can tim: ")
            new_word = input("Nhap tu khoa thay the: ")

            if old_word in description:
                count = description.count(old_word)
                description = description.replace(old_word, new_word)

                print("So lan xuat hien cua tu khoa:", count)
                print("Mo ta sau khi thay the:")
                print(description)

            else:
                print("Khong tim thay tu khoa trong mo ta")

    elif choice == 5:
        print("Thoat chuong trinh")
        break

    else:
        print("Lua chon khong hop le")