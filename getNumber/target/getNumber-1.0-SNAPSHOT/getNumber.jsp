<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.util.Random" %>
<%
  // 生成1-10的随机整数，存入session
  Random random = new Random();
  int targetNumber = random.nextInt(10) + 1;
  session.setAttribute("targetNumber", targetNumber);
  // 初始化猜测次数
  session.setAttribute("guessCount", 0);
  // 记录游戏开始时间（毫秒）
  session.setAttribute("startTime", System.currentTimeMillis());
%>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>猜数字游戏</title>
  <style>
    body {background-color: #00ffff; font-size: 24px; font-family: "宋体", sans-serif; margin: 50px;}
    input[type="text"] {width: 300px; height: 30px; font-size: 20px;}
    input[type="submit"] {font-size: 20px; padding: 5px 15px; margin-left: 10px;}
  </style>
</head>
<body>
<p>随机分给了你一个1到10之间的数，请猜！</p>
<p>输入你所猜的数</p>
<form action="result.jsp" method="post">
  <input type="text" name="guessNum" required>
  <input type="submit" value="送出">
</form>
</body>
</html>