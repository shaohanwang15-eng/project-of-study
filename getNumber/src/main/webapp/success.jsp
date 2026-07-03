<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
  // 防直接访问，无session数据跳回初始化页面
  Integer target = (Integer) session.getAttribute("targetNumber");
  Integer count = (Integer) session.getAttribute("guessCount");
  Long startTime = (Long) session.getAttribute("startTime");
  if (target == null || count == null || startTime == null) {
    response.sendRedirect("getNumber.jsp");
    return;
  }
  // 计算游戏用时（毫秒转秒）
  long useTime = (System.currentTimeMillis() - startTime) / 1000;
%>
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>猜对了</title>
  <style>
    body {background-color: #00ffff; font-size: 24px; font-family: "宋体", sans-serif; margin: 50px;}
    a {color: #0000cc;}
  </style>
</head>
<body>
<p>恭喜你，猜对了</p>
<p>您共猜了<%= count %>次</p>
<p>用时<%= useTime %>秒。</p>
<p>这个数字就是<%= target %></p>
<p>您必须关掉浏览器才能获得新的数，或者<a href="getNumber.jsp">点击这里重新开始游戏</a></p>
</body>
</html>