var mysql = require('mysql')

var con = mysql.createConnection({
    host:"localhost",
    user:"bharath",
    password:"",
    database:"mysql"
})

con.connect(function(err){
    if(err)throw err;
    sql="INSERT into pizza_bot(order_id,Name,phone_no,Address,order_name)values(13223,'bharath','9866677730','Avinashi','Paneer_Pizza')"
    con.query(sql,function(err,result){
    if(err)throw err;
    console.log("1 row added")
    })
})