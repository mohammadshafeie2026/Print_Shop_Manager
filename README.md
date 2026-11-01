# 🖨️ Print Shop Management System

### A Python Desktop Application for Printing Shop Management

یک نرم‌افزار دسکتاپ برای مدیریت مشتریان، سفارش‌های چاپ، محاسبه هزینه‌ها و ذخیره‌سازی اطلاعات، توسعه‌یافته با زبان برنامه‌نویسی Python.

---

## 📌 معرفی پروژه | Project Overview

این پروژه با هدف مدیریت ساده و یکپارچه فرایندهای اصلی یک چاپخانه طراحی و پیاده‌سازی شده است.

نرم‌افزار امکان ثبت و مدیریت اطلاعات مشتریان، ثبت سفارش‌های چاپ، محاسبه هزینه چاپ، لیتوگرافی و سلفون را از طریق یک رابط گرافیکی فراهم می‌کند.

این پروژه با استفاده از مفاهیم برنامه‌نویسی شیءگرا (OOP)، اعتبارسنجی داده‌ها، مدیریت فایل‌ها و معماری لایه‌ای توسعه داده شده است.

## ✨ امکانات اصلی | Features

- ثبت و مدیریت مشتریان
- ثبت سفارش‌های چاپ
- اتصال هر سفارش به مشتری مربوطه
- ثبت تاریخ سفارش و تاریخ تحویل
- اعتبارسنجی اطلاعات ورودی
- محاسبه هزینه چاپ بر اساس تعداد برگ
- محاسبه هزینه لیتوگرافی بر اساس تعداد رنگ
- محاسبه هزینه سلفون بر اساس ابعاد و تعداد برگ
- محاسبه قیمت نهایی سفارش
- ذخیره‌سازی و بازیابی اطلاعات با استفاده از Pickle
- رابط گرافیکی با Tkinter
- مدیریت خطاها و ورودی‌های نامعتبر

## 🛠️ Technologies & Concepts

| Technology | Usage |
|---|---|
| Python | Core Programming Language |
| Tkinter | Graphical User Interface |
| OOP | Object-Oriented Programming |
| Pickle | Data Persistence |
| OS | File Management |
| Exception Handling | Error Management |
| Properties | Getter & Setter |
| Regular Expressions | Input Validation |
| Git & GitHub | Version Control |

## 🏗️ Project Architecture

پروژه با ساختار ماژولار و تفکیک مسئولیت‌ها طراحی شده است.

```text
Print-Shop-Manager/
│
├── business_logic/
│   ├── customer_service.py
│   ├── order_service.py
│   └── pricing_price.py
│
├── controller/
│   ├── customer_controller.py
│   ├── order_controller.py
│   └── pricing_controller.py
│
├── data/
│
├── data_access/
│   ├── customer_repository.py
│   └── order_repository.py
│
├── model/
│   ├── customer.py
│   ├── order.py
│   └── pricing.py
│
├── test/
│
├── tools/
│   └── validation.py
│
├── view/
│   ├── main_window.py
│   ├── customer_window.py
│   ├── order_window.py
│   └── pricing_window.py
│
├── .gitignore
└── main.py
```

### Architecture Layers

- **Model:** تعریف ساختار داده‌ها و کلاس‌های اصلی.
- **Data Access:** ذخیره‌سازی و بازیابی اطلاعات.
- **Business Logic:** پیاده‌سازی قوانین و محاسبات برنامه.
- **Controller:** ارتباط میان رابط کاربری و منطق برنامه.
- **View:** طراحی رابط گرافیکی.
- **Tools:** ابزارهای کمکی مانند اعتبارسنجی اطلاعات.

## 📦 Main Classes

پروژه شامل سه کلاس اصلی است:

### 1. Customer
مدیریت اطلاعات مشتری شامل شناسه، نام، نام خانوادگی و شماره تماس.

### 2. Order
مدیریت سفارش چاپ شامل مشتری، تاریخ سفارش، تاریخ تحویل، ابعاد کار، تعداد برگ و تعداد رنگ.

### 3. Pricing
مدیریت تعرفه‌های چاپ، لیتوگرافی و سلفون.

## 💰 Pricing Logic

محاسبه قیمت نهایی بر اساس سه بخش انجام می‌شود:

1. **Printing Cost:** هزینه چاپ بر اساس تعداد بسته‌های ۵۰۰۰ برگی.
2. **Lithography Cost:** تعداد رنگ × هزینه هر زینک.
3. **Cellophane Cost:** طول × عرض × تعداد برگ × هزینه هر سانتی‌متر مربع.

قیمت نهایی از مجموع این سه بخش محاسبه می‌شود.

> تعرفه پایه چاپ در نسخه فعلی برنامه، ۲۵ میلیون تومان به ازای هر ۵۰۰۰ برگ است.

## 🚀 Installation & Execution

### Prerequisites

- Python
- PyCharm یا هر محیط توسعه پایتون
- Tkinter

### Run the Application

ابتدا مخزن پروژه را دریافت کنید:

```bash
git clone https://github.com/mohammadshafeie2026/Print_Shop_Manager.git
```

وارد پوشه پروژه شوید:

```bash
cd Print_Shop_Manager
```

سپس برنامه را اجرا کنید:

```bash
python main.py
```

## 🗄️ Data Storage

اطلاعات مشتریان و سفارش‌ها با استفاده از ماژول `pickle` ذخیره و بازیابی می‌شوند.

فایل‌های داده در پوشه `data` نگهداری می‌شوند و برنامه در صورت نبود فایل‌های ذخیره‌سازی، فهرست خالی را در نظر می‌گیرد.

## 🎯 Project Goals

اهداف اصلی این پروژه:

- پیاده‌سازی عملی مفاهیم برنامه‌نویسی شیءگرا در Python
- آشنایی با معماری ماژولار و تفکیک مسئولیت‌ها
- طراحی رابط گرافیکی با Tkinter
- مدیریت داده‌ها و فایل‌ها
- پیاده‌سازی اعتبارسنجی و مدیریت خطا
- توسعه یک نرم‌افزار کاربردی با استفاده از Python

## 🔮 Future Improvements

برنامه در آینده قابلیت توسعه به بخش‌های زیر را دارد:

- گزارش‌گیری و تحلیل داده‌های چاپخانه
- جست‌وجو و ویرایش اطلاعات مشتریان و سفارش‌ها
- مدیریت وضعیت سفارش‌ها
- توسعه رابط کاربری با ظاهر مدرن‌تر
- افزودن سیستم گزارش مالی

## 👨‍💻 Developer

**Mohammad Shafeie**

Python Developer | Physics Teacher | AI Enthusiast

GitHub: [@mohammadshafeie2026](https://github.com/mohammadshafeie2026)

**Repository:** [Print Shop Management System](https://github.com/mohammadshafeie2026/Print_Shop_Manager)

---

*Developed with Python and a focus on practical software engineering.*