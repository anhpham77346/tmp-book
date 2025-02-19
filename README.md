# Thiết Lập Dự Án

## Tạo Người Dùng Quản Trị

Để tạo một người dùng quản trị cho dự án Django của bạn, hãy làm theo các bước sau:

1. Mở terminal và điều hướng đến thư mục dự án của bạn.

2. Chạy lệnh sau để tạo một superuser:

    ```bash
    python manage.py createsuperuser
    ```

3. Bạn sẽ được yêu cầu nhập tên người dùng, địa chỉ email và mật khẩu cho superuser mới. Điền vào các thông tin cần thiết.

4. Sau khi tạo thành công superuser, bạn có thể đăng nhập vào trang quản trị Django bằng thông tin đăng nhập bạn đã cung cấp.

Vậy là xong! Bạn đã thiết lập xong người dùng quản trị cho dự án Django của mình.

## Xem Cấu Hình Database

Để xem cấu hình database trong dự án Django của bạn, hãy làm theo các bước sau:

1. Mở file `settings.py` trong thư mục dự án của bạn.

2. Tìm biến `DATABASES`. Cấu hình mặc định sẽ trông giống như sau:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / "db.sqlite3",
        }
    }
    ```

3. Nếu bạn đang sử dụng một loại database khác, cấu hình sẽ khác. Ví dụ, nếu bạn sử dụng PostgreSQL, cấu hình có thể trông như sau:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

4. Điều chỉnh các thông số trong biến `DATABASES` theo cấu hình database bạn đang sử dụng.

Vậy là xong! Bạn đã xem và có thể chỉnh sửa cấu hình database trong dự án Django của mình.