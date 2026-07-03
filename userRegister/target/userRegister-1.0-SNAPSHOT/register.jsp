<%@ page contentType="text/html;charset=UTF-8" %>
<html>
<head>
  <title>用户注册</title>
</head>
<body>
<h2>用户注册</h2>
<%-- 显示错误信息 --%>
<% if (request.getAttribute("errorMsg") != null) { %>
<p style="color: red;"><%= request.getAttribute("errorMsg") %></p>
<% } %>

<form action="registerServlet" method="post">
  <label>手机号：</label>
  <label>
    <input type="text" name="phone" value="${param.phone}" required>
  </label><br><br>

  <label>昵称：</label>
  <label>
    <input type="text" name="nickname" value="${param.nickname}" required>
  </label><br><br>

  <label>密码：</label>
  <label>
    <input type="password" name="password" required>
  </label><br><br>

  <label>再次输入密码：</label>
  <label>
    <input type="password" name="rePassword" required>
  </label><br><br>

  <input type="submit" value="注册">
</form>
</body>
</html>