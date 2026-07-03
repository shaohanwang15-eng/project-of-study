package com.example.userregister;


import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebServlet("/registerServlet")
public class RegisterServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 1. 设置请求编码，解决中文乱码
        request.setCharacterEncoding("UTF-8");
        response.setContentType("text/html;charset=UTF-8");

        // 2. 获取表单参数
        String phone = request.getParameter("phone");
        String nickname = request.getParameter("nickname");
        String password = request.getParameter("password");
        String rePassword = request.getParameter("rePassword");

        // 3. 校验信息
        String errorMsg = null;

        // 校验手机号：11位数字
        if (phone == null || !phone.matches("\\d{11}")) {
            errorMsg = "手机号必须是11位数字";
        }
        // 校验两次密码是否一致
        else if (!password.equals(rePassword)) {
            errorMsg = "两次输入的密码不一致";
        }

        // 4. 处理结果
        if (errorMsg != null) {
            // 校验失败：回传错误信息和用户输入，转发到注册页
            request.setAttribute("errorMsg", errorMsg);
            request.setAttribute("phone", phone);
            request.setAttribute("nickname", nickname);
            request.getRequestDispatcher("/register.jsp").forward(request, response);
        } else {
            // 校验成功：跳转到成功页，传递手机号和昵称
            request.setAttribute("phone", phone);
            request.setAttribute("nickname", nickname);
            request.getRequestDispatcher("/success.jsp").forward(request, response);
        }
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request, response);
    }
}