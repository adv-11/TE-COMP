<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
        <style>
          table {
            border-collapse: collapse;
            width: 100%;
          }
          th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
          }
          th {
            background-color: #f2f2f2;
          }
        </style>
      </head>
      <body>
        <h2>Employee Information</h2>
        <table>
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
         
            <th>Contact No</th>
            <th>Address</th>
            <th>Gender</th>
            <th>Designation</th>
            
            <th>Salary</th>
            
          </tr>
          <xsl:apply-templates select="employees/employee"/>
        </table>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="employee">
    <tr>
      <td><xsl:value-of select="empName/fname"/></td>
      <td><xsl:value-of select="empName/lname"/></td>
      
      <td><xsl:value-of select="contactno"/></td>
      <td><xsl:value-of select="address"/></td>
      <td><xsl:value-of select="gender"/></td>
      <td><xsl:value-of select="designation"/></td>
      
      <td><xsl:value-of select="salary"/></td>
      
    </tr>
  </xsl:template>

</xsl:stylesheet>

