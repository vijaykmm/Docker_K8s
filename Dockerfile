FROM tomcat
ADD addressbook.war /user/local/tomcat/webaps/addressbook.war
CMD ["catalina.sh", "run"]
