<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<form action="add1.jsp" method="get">
		<input type="text" name="t1">
		<!-- <input type="text" name="t2"> -->
		<input type="submit" name="Add">
	</form>
<%
  // int x=Integer.parseInt(request.getParameter("t1"));
  // int y=Integer.parseInt(request.getParameter("t2"));
  String d=request.getParameter("t1");
  // int c=x+y;
  out.println(d);
%>
</body>
</html>