import json
import os

# Đường dẫn tới file lưu trữ dữ liệu
DATA_FILE = "TEST_DICT.json"

# Nạp dữ liệu từ file JSON vào danh sách khi khởi động chương trình
players_list = []
if os.path.exists(DATA_FILE):
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            players_list = json.load(file)
    except Exception:
        players_list = []

# Vòng lặp điều khiển chương trình chính
while True:
    print("\n==================== QUAN LY CAU THU ====================")
    print("1. Hien thi danh sach cau thu")
    print("2. Them moi cau thu")
    print("3. Cap nhat chi so cau thu")
    print("4. Xoa cau thu")
    print("5. Tim kiem cau thu")
    print("6. Sap xep danh sach cau thu")
    print("7. Thong ke cau thu theo danh hieu")
    print("8. Thong ke so luong cau thu theo danh hieu")
    print("9. Hien thi cau thu co danh hieu nhieu/it nhat")
    print("0. Thoat chuong trinh")
    print("=========================================================")
    
    choice = input("Nhap lua chon cua ban (0-9): ").strip()
    
    match choice:
        case '1':
            # Hiển thị danh sách cầu thủ dưới dạng bảng
            if not players_list:
                print("\nDanh sach cau thu hien dang trong!")
            else:
                print("\n" + "="*85)
                print(f"{'ID':<10}{'Player Name':<25}{'Matches':<10}{'Goals':<12}{'Assists':<10}{'Score':<10}{'Title':<10}")
                print("-" * 85)
                for p in players_list:
                    print(f"{p['player_id']:<10}{p['name']:<25}{p['matches']:<10}{p['goals']:<12}{p['assists']:<10}{p['performance_score']:<10}{p['title']:<10}")
                print("="*85)
                
        case '2':
            # Thêm mới cầu thủ
            print("\n--- THEM MOI CAU THU ---")
            
            # Validate ID không được trống và không trùng
            while True:
                player_id = input("Nhap Ma cau thu: ").strip()
                if not player_id:
                    print("Loi: Ma cau thu khong duoc de trong!")
                    continue
                
                is_duplicate = False
                for p in players_list:
                    if p['player_id'].lower() == player_id.lower():
                        is_duplicate = True
                        break
                
                if is_duplicate:
                    print("Loi: Ma cau thu da ton tai! Vui loi nhap ma khac.")
                else:
                    break

            name = input("Nhap Ten cau thu: ").strip()
            
            # Validate Matches >= 0
            while True:
                try:
                    matches = int(input("Nhap So tran da dau: "))
                    if matches >= 0:
                        break
                    print("Loi: Gia tri phai lon hon hoac bang 0!")
                except ValueError:
                    print("Loi: Dinh dang khong hop le. Vui long nhap so nguyen!")
            
            # Validate Goals >= 0
            while True:
                try:
                    goals = int(input("Nhap So ban thang: "))
                    if goals >= 0:
                        break
                    print("Loi: Gia tri phai lon hon hoac bang 0!")
                except ValueError:
                    print("Loi: Dinh dang khong hop le. Vui long nhap so nguyen!")
            
            # Validate Assists >= 0
            while True:
                try:
                    assists = int(input("Nhap So kien tao: "))
                    if assists >= 0:
                        break
                    print("Loi: Gia tri phai lon hon hoac bang 0!")
                except ValueError:
                    print("Loi: Dinh dang khong hop le. Vui long nhap so nguyen!")

            # Tự động tính điểm thành tích và danh hiệu
            performance_score = (goals * 2) + assists
            if performance_score > 40:
                title = "Gold"
            elif performance_score > 20:
                title = "Silver"
            else:
                title = "Bronze"

            # Tạo dictionary cầu thủ mới và thêm vào list
            new_player = {
                "player_id": player_id,
                "name": name,
                "matches": matches,
                "goals": goals,
                "assists": assists,
                "performance_score": performance_score,
                "title": title
            }
            players_list.append(new_player)
            
            # Lưu vào file JSON
            try:
                with open(DATA_FILE, "w", encoding="utf-8") as file:
                    json.dump(players_list, file, ensure_ascii=False, indent=4)
                print(f"Them cau thu '{name}' thanh cong!")
            except Exception as e:
                print(f"Loi luu file: {e}")
                
        case '3':
            # Cập nhật thông tin chỉ số cầu thủ
            print("\n--- CAP NHAT CHI SO CAU THU ---")
            player_id = input("Nhap Ma cau thu can cap nhat: ").strip()
            
            found = False
            for p in players_list:
                if p['player_id'].lower() == player_id.lower():
                    found = True
                    print(f"Tim thay cau thu: {p['name']}")
                    
                    # Validate số bàn thắng mới
                    while True:
                        try:
                            p['goals'] = int(input(f"Nhap so Ban thang moi (Hien tai {p['goals']}): "))
                            if p['goals'] >= 0:
                                break
                            print("Loi: Gia tri phai lon hon hoac bang 0!")
                        except ValueError:
                            print("Loi: Dinh dang khong hop le!")
                            
                    # Validate số kiến tạo mới
                    while True:
                        try:
                            p['assists'] = int(input(f"Nhap so Kien tao moi (Hien tai {p['assists']}): "))
                            if p['assists'] >= 0:
                                break
                            print("Loi: Gia tri phai lon hon hoac bang 0!")
                        except ValueError:
                            print("Loi: Dinh dang khong hop le!")
                    
                    # Tính toán lại Score và Title
                    p['performance_score'] = (p['goals'] * 2) + p['assists']
                    if p['performance_score'] > 40:
                        p['title'] = "Gold"
                    elif p['performance_score'] > 20:
                        p['title'] = "Silver"
                    else:
                        p['title'] = "Bronze"
                    
                    # Lưu lại thay đổi
                    try:
                        with open(DATA_FILE, "w", encoding="utf-8") as file:
                            json.dump(players_list, file, ensure_ascii=False, indent=4)
                        print("Cap nhat thong tin thanh cong!")
                    except Exception as e:
                        print(f"Loi luu file: {e}")
                    break
            
            if not found:
                print("Loi: Khong tim thay Ma cau thu nay.")
                
        case '4':
            # Xóa cầu thủ
            print("\n--- XOA CAU THU ---")
            player_id = input("Nhap Ma cau thu can xoa: ").strip()
            
            found = False
            for p in players_list:
                if p['player_id'].lower() == player_id.lower():
                    found = True
                    confirm = input(f"Ban co chac chan muon xoa cau thu {p['name']}? (Y/N): ").strip().lower()
                    if confirm == 'y':
                        players_list.remove(p)
                        try:
                            with open(DATA_FILE, "w", encoding="utf-8") as file:
                                json.dump(players_list, file, ensure_ascii=False, indent=4)
                            print("Da xoa cau thu thanh cong.")
                        except Exception as e:
                            print(f"Loi luu file: {e}")
                    else:
                        print("Da huy thao tac xoa.")
                    break
            
            if not found:
                print("Loi: Khong tim thay Ma cau thu nay.")
                
        case '5':
            print("\n--- TIM KIEM CAU THU ---")
            keyword = input("Nhap Ten hoac Ma cau thu can tim: ").strip().lower()
            search_results = []
            
            for p in players_list:
                if keyword in p['player_id'].lower() or keyword in p['name'].lower():
                    search_results.append(p)
                    
            if search_results:
                print(f"\nTim thay {len(search_results)} ket qua phu hop:")
                print("\n" + "="*85)
                print(f"{'ID':<10}{'Player Name':<25}{'Matches':<10}{'Goals':<12}{'Assists':<10}{'Score':<10}{'Title':<10}")
                print("-" * 85)
                for p in search_results:
                    print(