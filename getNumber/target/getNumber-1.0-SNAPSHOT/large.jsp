<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>猜大了</title>
  <style>
    body {background-color: #00ffff; font-size: 24px; font-family: "宋体", sans-serif; margin: 50px;}
    input[type="text"] {width: 300px; height: 30px; font-size: 20px;}
    input[type="submit"] {font-size: 20px; padding: 5px 15px; margin-left: 10px;}
  </style>
</head>
<body>
<p>所猜的数比实际的数大，请再猜：</p>
<form action="result.jsp" method="post">
  <input type="text" name="guessNum" required>
  <input type="submit" value="送出">
</form>
</body>
</html>