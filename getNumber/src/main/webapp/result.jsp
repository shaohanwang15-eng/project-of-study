<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
  request.setCharacterEncoding("UTF-8");
  // 从session获取游戏数据，无数据则跳回初始化页面
  Integer target = (Integer) session.getAttribute("targetNumber");
  Integer count = (Integer) session.getAttribute("guessCount");
  Long startTime = (Long) session.getAttribute("startTime");
  if (target == null || count == null || startTime == null) {
    response.sendRedirect("getNumber.jsp");
    return;
  }

  // 获取用户输入，处理非数字异常
  String guessStr = request.getParameter("guessNum");
  int guessNum;
  try {
    guessNum = Integer.parseInt(guessStr);
  } catch (NumberFormatException e) {
    out.println("<script>alert('请输入有效的整数！');history.back();</script>");
    return;
  }

  // 校验数字范围
  if (guessNum < 1 || guessNum > 10) {
    out.println("<script>alert('请输入1到10之间的整数！');history.back();</script>");
    return;
  }

  // 猜测次数+1，更新到session
  count++;
  session.setAttribute("guessCount", count);

  // 对比数字，跳转对应页面
  if (guessNum == target) {
    request.getRequestDispatcher("success.jsp").forward(request, response);
  } else if (guessNum > target) {
    request.getRequestDispatcher("large.jsp").forward(request, response);
  } else {
    request.getRequestDispatcher("small.jsp").forward(request, response);
  }
%>