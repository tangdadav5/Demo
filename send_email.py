'''python发送邮件
SMTP:发送邮件的协议
python对smtp的支持有smtplib，email俩个模块
        email： 负责构造邮件
        smtplib：负责发送邮件
        纯文本：
        html格式：
        带附件的邮件:
'''

'''纯文本邮件'''
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_text():
    '''发送纯文本邮件'''
    #第一步：创建账号数据（transsnet）
    # smtpserver='hwhzsmtp.qiye.163.com'       #发送，邮件服务器
    # sender ='song.tang@transsnet.com'   #发送人账号
    # password='qEvK5zYgkz7GF43z'           #发送人的密码
    # revicer='603767855@qq.com'   #接收人

    #qq邮箱
    smtpserver = 'smtp.qq.com'  # 发送，邮件服务器
    sender = '603767855@qq.com'  # 发送人账号
    password = 'qyqjkxozzaynbfha'  # 发送人的密码
    revicer = 'song.tang@transsnet.com'  # 接收人

    #第二步：构建邮件内容，MIMEText构造
    content=MIMEText('hello1，第一次用python发邮件','plain','utf-8')

    #第三步：邮件的发送过程，smtplib
    serve = smtplib.SMTP(smtpserver,25)   #邮件服务器，和端口
    serve = smtplib.SMTP(smtpserver, 25)  # 邮件服务器，和端口
    serve.login(sender,password)        #先登录邮件服务器，
    serve.set_debuglevel(1)             #查看日志
    serve.sendmail(sender,revicer,content.as_string()) #1.发送人，2接收人 ，3将构建内容转换成字符串
    serve.quit()  #退出邮箱
    print("end")




def send_email_text_title():
    '''发送纯文本邮件,在第二步声明一下发件人和收件人的主题'''
    #第一步：创建账号数据
    smtpserver = 'hwhzsmtp.qiye.163.com'  # 发送，邮件服务器
    sender = 'song.tang@transsnet.com'  # 发送人账号
    password = 'qEvK5zYgkz7GF43z'  # 发送人的密码
    revicer = '603767855@qq.com;274522487@qq.com'  # 接收人

    #第二步：构建邮件内容，MIMEText构造
    content=MIMEText('hello2，第一次用python发邮件','plain','utf-8')
    content['From']=Header(sender,'utf-8')
    content['To']=revicer
    content['Subject']=Header("主题是自动化测试",'utf-8')



    #第三步：邮件的发送过程，smtplib
    serve=smtplib.SMTP(smtpserver,25)   #邮件服务器，和端口
    serve.login(sender,password)        #先登录邮件服务器，
    #serve.set_debuglevel(1)             #查看日志
    serve.sendmail(sender,revicer,content.as_string()) #1.发送人，2接收人 ，3将构建内容转换成字符串
    serve.quit()  #退出邮箱


'''html邮件：
html:描述网页的一种语言；一套标记标签
     起始标签<html>，结束标签</html>
     构建邮件内容模式：html
'''
def send_email_html():
    '''发送纯文本邮件,在第二步声明一下发件人和收件人的主题'''
    #第一步：创建账号数据
    smtpserver = 'hwhzsmtp.qiye.163.com'  # 发送，邮件服务器
    sender = 'song.tang@transsnet.com'  # 发送人账号
    password = 'qEvK5zYgkz7GF43z'  # 发送人的密码
    revicer = '603767855@qq.com'  # 接收人

    #第二步：构建邮件内容，MIMEText构造
    content=MIMEText('''<!DOCTYPE html>
<html lang="zh-cn">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <title>Weather API Test Report</title>
    <meta name="generator" content="BSTestRunner 0.8.4"/>
    <link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css">
    
<style type="text/css" media="screen">

/* -- css div popup ------------------------------------------------------------------------ */
.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    padding: 10px;
    background-color: #99CCFF;
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 10pt;
    width: 500px;
}

/* -- report ------------------------------------------------------------------------ */

#show_detail_line .label {
    font-size: 85%;
    cursor: pointer;
}

#show_detail_line {
    margin: 2em auto 1em auto;
}

#total_row  { font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }

</style>


    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="http://cdn.bootcss.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="http://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
<body>
<script language="javascript" type="text/javascript"><!--
output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}


function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}


function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}


function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}

/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
--></script>

<div class="container">
    <div class='heading'>
<h1>Weather API Test Report</h1>
<p><strong>Start Time:</strong> 2019-06-27 20:57:00</p>
<p><strong>Duration:</strong> 0:00:14.630837</p>
<p><strong>Status:</strong> <span class="text text-success">Pass <strong>3</strong></span></p>

<p class='description'>China city weather report</p>
</div>


    
<p id='show_detail_line'>
<span class="label label-primary" onclick="showCase(0)">Summary</span>
<span class="label label-danger" onclick="showCase(1)">Failed</span>
<span class="label label-default" onclick="showCase(2)">All</span>
</p>
<table id='result_table' class="table">
    <thead>
        <tr id='header_row'>
            <th>Test Group/Test case</td>
            <th>Count</td>
            <th>Pass</td>
            <th>Fail</td>
            <th>Error</td>
            <th>View</td>
        </tr>
    </thead>
    <tbody>
        
<tr class='text text-success'>
    <td>test_weather.WeatherTest</td>
    <td>3</td>
    <td>3</td>
    <td>0</td>
    <td>0</td>
    <td><a class="btn btn-xs btn-primary"href="javascript:showClassDetail('c1',3)">Detail</a></td>
</tr>

<tr id='pt1.1' class='hiddenRow'>
    <td class='text text-success'><div class='testcase'>test_popular1</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt1.2' class='hiddenRow'>
    <td class='text text-success'><div class='testcase'>test_popular2</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt1.3' class='hiddenRow'>
    <td class='text text-success'><div class='testcase'>test_popular3</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

    </tbody>
    <tfoot>
        <tr id='total_row'>
            <td>Total</td>
            <td>3</td>
            <td class="text text-success">3</td>
            <td class="text text-danger">0</td>
            <td class="text text-warning">0</td>
            <td>&nbsp;</td>
        </tr>
    </tfoot>
</table>

    <div id='ending'>&nbsp;</div>
</div>

</body>
</html>
''','html','utf-8')
    content['From']=Header(sender,'utf-8')
    content['To']=revicer
    content['Subject']=Header("主题是自动化测试",'utf-8')


    #第三步：邮件的发送过程，smtplib
    serve=smtplib.SMTP(smtpserver,25)   #邮件服务器，和端口
    serve.login(sender,password)        #先登录邮件服务器，
    serve.set_debuglevel(1)             #查看日志
    serve.sendmail(sender,revicer,content.as_string()) #1.发送人，2接收人 ，3将构建内容转换成字符串
    serve.quit()  #退出邮箱


#带附件

def send_email_addatt():
    '''发送纯文本邮件,在第二步声明一下发件人和收件人的主题'''
    # 第一步：创建账号数据
    smtpserver = 'hwhzsmtp.qiye.163.com'  # 发送，邮件服务器
    sender = 'song.tang@transsnet.com'  # 发送人账号
    password = 'qEvK5zYgkz7GF43z'  # 发送人的密码
    revicer = '603767855@qq.com;274522487@qq.com'  # 接收人
    # filename='D:\PythonCode\api_autotest\reports\2019-06-27 18_37_29test_report.html'
    filename=r'E:\12\intercase.xlsx'

    # 第二步：构建邮件内容，MIMEText构造
    # 构造附件1，传送当前目录下的 filename 文件
    att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="' + filename + '"'

    message = MIMEMultipart()
    message.attach(MIMEText('1038', 'plain', 'utf-8'))
    message['From'] = Header(sender, 'utf-8')
    message['To'] = revicer
    message['Subject'] = Header("主题是自动化测试", 'utf-8')
    message.attach(att1)

    # 第三步：邮件的发送过程，smtplib
    serve = smtplib.SMTP(smtpserver, 25)  # 邮件服务器，和端口
    serve.login(sender, password)  # 先登录邮件服务器，
    # serve.set_debuglevel(1)             #查看日志
    serve.sendmail(sender, revicer, message.as_string())  # 1.发送人，2接收人 ，3将构建内容转换成字符串
    serve.quit()  # 退出邮箱




# send_email_text()
# send_email_text_title()
# send_email_html()
send_email_addatt()
