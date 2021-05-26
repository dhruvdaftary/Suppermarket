<h1 align="center"> :fire: Supermarket :fire:</h1>
<div align="center">
  
  <h2> Add, update and purchase items along with separate databases for each customers </h2>

</div>

<div align="center">
  
[![](https://img.shields.io/badge/Made_with-Sqlite3-white?style=for-the-badge&logo=Sqlite3)](https://https://www.mysql.com/ "MySQL")

</div>

  
### To run this project :

Clone the project -
```
  $ https://github.com/dhruvdaftary/Suppermarket.git
```
  
Install all the requirements -
```
  $ pip install -r requirements.txt
 ``` 
Run the following commands -

 You need to create a Database called supermarket for this,
 Run the following line only once for that.
``` 
  $ mycursor.execute("CREATE DATABASE supermarket")
``` 
 To create a Table for the seller,
 Run the folllowing line only once for that.
 ``` 
  $ mycursor.execute ("CREATE TABLE seller_items ( name VARCHAR(255), purchased_price VARCHAR(255), selling_price VARCHAR(255), quantity VARCHAR(255), profit VARCHAR (255))")

  ``` 
To run the file -

$ Open terminal
$ Navigate the terminal to directory where script is located using cd command
$ Run following codes
``` 
 $ python3 Supermarket(with MySQL database).py
 $ python3 Supermarket(without database).py
 ```
 
- #### If you have any improvements create an issue and if you want you can also make a pull request for the same 

---


---
<h3 align="center"><b>Developed with :heart: by <a href="https://github.com/dhruvdaftary">Dhruv Daftary</a> </b></h1>
