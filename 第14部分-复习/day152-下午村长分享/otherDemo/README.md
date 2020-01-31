<div align="center">
  <img src="http://47.94.172.250:33334/static/frontend/head_portrait/logo@2x.png?t=1542252961.100895" width="150px">
  <br>
  <strong>ThirtyPartyDemo</strong>
</div>

# 开发环境

* Python (3.6.2)
* Django (1.11.3)

# 配置开发环境

## 使用虚拟环境(virturalenv)

```
pip3 install virtualenv

切换到项目目录下, 执行下面的命令
source venv/bin/activate

pip install -r requirements.txt

```

## 生成表结构

```
python manage.py makemigrations

python manage.py migrate
```

## 启动项目

```
python manage.py runserver 0.0.0.0:9527
```

## 根据信息访问具体的路由即可

## 常见问题

### 第一次执行这条语句报No changes detected

* 问题

```
python manage.py makemigrations
```

* 解决

在`APP`创建目录 migrations 并在里面创建__init__.py
```
mkdir APP_NAME/migrations
touch APP_NAME/migrations/__init__.py
```
