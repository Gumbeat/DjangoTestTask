## Setup and launch    
    pip install -r requirements.txt
    python manage.py runserver 
#
## Docker
    docker build .
    docker run -d --network=host    
#
## URLS
- [/organizations/](http://127.0.0.1:8000/organizations/) - *Список всех заведений*
- [/organization/{id}](http://127.0.0.1:8000/organization/1/) - *Информация о выбранном заведении*
- [/organizations/{id}](http://127.0.0.1:8000/organizations/1/) - *Информация о заведениях, находящихся в выбранном районе*
- [/products/](http://127.0.0.1:8000/products/) - *Список всех товаров*
- [/product/{id}](http://127.0.0.1:8000/product/1/) - *Информация о выбранном товаре*
#  
## Filter parameters
- *product_name* - фильтрация по названию товара, находящегося в заведениях
- *category* - фильтрация по категории товаров
- *price_gte* - фильтрация по значению большему или равному цене товаров
- *price_lte* - фильтрация по значению меньшему или равному цене товаров
#