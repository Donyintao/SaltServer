Soil Service Manager Platform
==============================================

[![Python Version](https://img.shields.io/badge/Python--2.7-paasing-green.svg)](https://img.shields.io/badge/Python--3.6-paasing-green.svg)
[![Django Version](https://img.shields.io/badge/Django--1.11.6-paasing-green.svg)](https://img.shields.io/badge/Django--1.11.0-paasing-green.svg)

> SoilServer 现有功能:

- 资产管理
- 域名管理
- 故障管理

## 部署

### 安装依赖
```
pip install suit
pip install django==1.11.6
```
### 修改配置
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SoilServer',
        'USER': 'django',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
### 初始化数据
```
python manage.py makemigrations
python manage.py migrate
```
### 登录
```
# 创建用户
python manage.py createsuperuser
# 启动服务
python manage.py runserver http://127.0.0.1:8000
```

![SaltServer](https://raw.githubusercontent.com/Donyintao/SoilServer/master/doc/images/hosts_list.jpg)
![SaltServer](https://raw.githubusercontent.com/Donyintao/SoilServer/master/doc/images/hosts_add.jpg)
![SaltServer](https://raw.githubusercontent.com/Donyintao/SoilServer/master/doc/images/hosts_details.jpg)
![SaltServer](https://raw.githubusercontent.com/Donyintao/SoilServer/master/doc/images/bind_add.jpg)
![SaltServer](https://raw.githubusercontent.com/Donyintao/SoilServer/master/doc/images/bind_list.jpg)
![SaltServer](https://raw.githubusercontent.com/Donyintao/SoilServer/master/doc/images/faults_list.jpg)
![SaltServer](https://raw.githubusercontent.com/Donyintao/SoilServer/master/doc/images/faults_add.jpg)
![SaltServer](https://raw.githubusercontent.com/Donyintao/SoilServer/master/doc/images/faults_details.jpg)
