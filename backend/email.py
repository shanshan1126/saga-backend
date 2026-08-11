import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
code_to_dept = {
    "TUT": "教学部",
    "CM": "行研部",
    "IT": "IT部",
    "HR": "人事部",
    "PR": "宣传部",
    "FAL": "财法部",
    "LIA": "外联部",
}
dept_to_file_url = {
    "TUT": "https://lcny1jsoyn29.feishu.cn/drive/folder/FOIXfXVUilAe0LdlLiWcpMRAnHB",
    "CM": "https://lcny1jsoyn29.feishu.cn/drive/folder/BCNefGzEMlvmmsdy2rucbo9ynIh",
    "IT": "https://lcny1jsoyn29.feishu.cn/drive/folder/Fp0bfAOvOlPuQJdObPnc4iiWnih",
    "HR": "https://lcny1jsoyn29.feishu.cn/drive/folder/Pgisffl4ClzunkdWLJIc7xeDnSe",
    "PR": "https://lcny1jsoyn29.feishu.cn/drive/folder/VTxGf4cj9lsRo2dnAYTcaKkFniA",
    "FAL": "https://lcny1jsoyn29.feishu.cn/drive/folder/UwbCfDBFolKepHdWJY0couAfnQh",
    "LIA": "https://lcny1jsoyn29.feishu.cn/drive/folder/S6dtfSEmxlNl1edqe93czW4Hn14",
}
dept_to_eng = {
    "TUT": "Teaching",
    "CM": "Class-management",
    "IT": "IT",
    "HR": "HR",
    "PR": "Publicity",
    "FAL": "Finance-and-Legal",
    "LIA": "Liaison",
}

def compose_writing_task_email(id, name, dept, ddl):
    file_url = dept_to_file_url.get(dept, "http://example.com/default_exam")
    content = f"""
  <html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Simple Transactional Email</title>
    <style media="all" type="text/css">
    /* -------------------------------------
    GLOBAL RESETS
------------------------------------- */
    
    body {{
      font-family: Helvetica, sans-serif;
      -webkit-font-smoothing: antialiased;
      font-size: 16px;
      line-height: 1.3;
      -ms-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
      
    }}
    
    table {{
      border-collapse: separate;
      /* mso-table-lspace: 0pt;
      mso-table-rspace: 0pt; */
      width: 100%;
    }}
    
    table td {{
      font-family: Helvetica, sans-serif;
      font-size: 16px;
      vertical-align: top;
    }}
    /* -------------------------------------
    BODY & CONTAINER
------------------------------------- */
    
    body {{
      background-color:rgb(255,189,89);
      margin: 0;
      padding: 0;
    }}

    .body {{ 
      width: 100%;
    }}
    .signature-thin{{
      margin-top: 3em;
      line-height: 1;
      font-size: 12px;
    }}
    .signature-plus {{
      margin-top: 2em;
      line-height: 0.4;
      font-style: italic;
    }}
    .highlight {{
      font-weight: bold;
      color: #dcac0f;
    }}
    .highlight-thin {{
      color: #dcac0f;
      font-style:oblique;
    }}
    .des-post{{
        font-size: 14px;
    }} 
    .container {{
      margin: 0 auto !important;
      max-width: 600px;
      padding: 0;
      padding-top: 24px;
      width: 600px;
    }}
    
    .content {{
      box-sizing: border-box;
      display: block;
      margin: 0 auto;
      max-width: 600px;
      padding: 0;
    }}
    /* -------------------------------------
    HEADER, FOOTER, MAIN
------------------------------------- */
    
    .main {{
      background: #f6f6e0;
      border: 1px solid #eaebed;
      border-radius: 16px;
      width: 100%;
    }}
    
    .wrapper {{
      box-sizing: border-box;
      padding: 24px;
    }}
    
    .footer {{
      clear: both;
      padding-top: 24px;
      padding-bottom: 5%;
      text-align: center;
      width: 100%;
    }}
    
    .footer td,
    .footer p,
    .footer span,
    .footer a {{
      color: #d37d37;
      font-size: 16px;
      text-align: center;
    }}
    /* -------------------------------------
    TYPOGRAPHY
------------------------------------- */
    
    p {{
      font-family: Helvetica, sans-serif;
      font-size: 16px;
      font-weight: normal;
      margin: 0;
      margin-bottom: 16px;
    }}
    a:link{{		/*默认状态*/
      color: #dcac0f;
    }}
    a:visited{{	/*浏览过的*/
      color:rgb(255,167,27);
    }}
    a:hover{{	/*悬浮状态*/
      color:rgb(255,195,33);
    }}
    a:active{{	/*激活过的*/
      color:rgb(255,141,27);
    }}
    .namestyle{{
      font-style: italic;
      font-weight: bold;
      color: #dcac0f;
    }}
    /* -
    OTHER STYLES THAT MIGHT BE USEFUL
------------------------------------- */
    .preheader {{
      color: transparent;
      display: none;
      height: 0;
      max-height: 0;
      max-width: 0;
      opacity: 0;
      overflow: hidden;
      /* mso-hide: all; */
      visibility: hidden;
      width: 0;
    }}
    
    .powered-by a {{
      text-decoration: none;
    }}
    
    /* -------------------------------------
    RESPONSIVE AND MOBILE FRIENDLY STYLES
------------------------------------- */
    
    @media only screen and (max-width: 640px) {{
      .main p,
      .main td,
      .main span {{
        font-size: 16px !important;
      }}
      .wrapper {{
        padding: 8px !important;
      }}
      .content {{
        padding: 0 !important;
      }}
      .container {{
        padding: 0 !important;
        padding-top: 8px !important;
        width: 100% !important;
      }}
      .main {{
        border-left-width: 0 !important;
        border-radius: 0 !important;
        border-right-width: 0 !important;
      }}
    }}
    /* -------------------------------------
    PRESERVE THESE STYLES IN THE HEAD
------------------------------------- */
    
    @media all {{
      .ExternalClass {{
        width: 100%;
      }}
      .ExternalClass,
      .ExternalClass p,
      .ExternalClass span,
      .ExternalClass font,
      .ExternalClass td,
      .ExternalClass div {{
        line-height: 100%;
      }}
      .apple-link a {{
        color: inherit !important;
        font-family: inherit !important;
        font-size: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        text-decoration: none !important;
      }}
      #MessageViewBody a {{
        color: inherit;
        text-decoration: none;
        font-size: inherit;
        font-family: inherit;
        font-weight: inherit;
        line-height: inherit;
      }}
    }}
    /* picture */

   .pic-top{{
     display: flex;
     flex-direction: column;
     text-align: center;
     justify-content: center;
     align-items: center;
     width: 100%;
   }}
   .pic-top img {{
      width: 100%;
      height: auto;
    }}
   
    </style>
  </head>
  <body>
    <div class="pic-top">
      <img src="http://saga-xingguang.com/static/public/imgs/writing-task-email-banner.jpg" alt="">
    </div>
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body">
      <tr>
        <td>&nbsp;</td>
        <td class="container">
          <div class="content">

            <!-- START CENTERED WHITE CONTAINER -->
            <span class="preheader">SAGA星光·第五期 - 笔试邀请</span>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="main">

              <!-- START MAIN CONTENT AREA -->
              <tr>
                <td class="wrapper">
                  <p>亲爱的{name}同学,</p>
                  <p>您好!</p>
                  <p>感谢您参加志行会SAGA星光线上课堂项目<span class="highlight">{code_to_dept[dept]}</span>的招募。我们诚挚地邀请您参加此次招募的第一轮环节——笔试环节。(请仔细查看笔试考核相关文件)</p>
                  <p>您可以从下方的链接中下载笔试文件，并在原文档上进行编辑。如您所申请的组别有录制试讲要求，请您仔细查看附件相关内容。<br>请您在收到笔试考核的<span class="highlight">七天内({ddl} 前)</span>将您的所有笔试文件全部放至一个PDF文件内并上传至下方提供的提交链接中，若逾期提交，我们将视为主动放弃。</p>
                  
                  <p>您的文件下载链接是: <a href="{file_url}">下载笔试题目</a>    ，您的文件提交链接是:  <a href="http://www.saga-xingguang.com/appreciation/volunteers/upload-writing-task?id={id}">提交笔试文件</a></p>
        
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary" >
                    <tbody>
                      <tr>
                        <td align="left">
                          <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                            <tbody>                             
                            </tbody>           
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <p>如果您对以上安排有任何疑问或要求，请您尽快通过邮箱与我们联络，我们将与您做进一步交流。
                  <br>
                  <span class="des-post">技术支持邮箱：</span><span class="highlight-thin">support@saga-xingguang.com</span>
                  <br>
                  <span class="des-post">人事部邮箱：</span><span class="highlight-thin">human-resource@saga-xingguang.com</span>
                  </p>
                  <div class="signature-thin">
                    <p>顺颂，<br>夏祺</p>
                  </div>
                  <div class="signature-thin">
                    <p>志行会SAGA星光项目组·{code_to_dept[dept]}敬上</p>
                    <p>---SAGA星光团队 </p>
                  </div>
                  
                </td>
              </tr>

              <!-- END MAIN CONTENT AREA -->
              </table>

            <!-- START FOOTER -->
            <div class="footer">
              <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                <tr>
                  <td class="content-block">
                    <span class="apple-link">微信公众号：星光SAGA</span>
                    <br>
                    
                  </td>
                </tr>
                <tr>
                  <!-- <td class="content-block powered-by">
                    Powered by <a href="http://htmlemail.io">HTMLemail.io</a>
                  </td> -->
                </tr>
              </table>
            </div>

            <!-- END FOOTER -->
            
<!-- END CENTERED WHITE CONTAINER --></div>
        </td>
        <td>&nbsp;</td>
      </tr>
    </table>
    
  </body>
</html>


"""
    return content

def send_email_with_no_reply(to, subject, content) -> bool:
    try:
        sender = "no-reply@saga-xingguang.com"
        server = smtplib.SMTP('smtp.feishu.cn', 587)
        server.starttls()
        server.login(sender, os.environ.get("SAGA_NO_REPLY_EMAIL_PASSWORD", ""))
        
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "【SAGA】2024-2025年度志愿者招募笔试邀请函"
        msg["From"] = sender
        msg["To"] = to
        msg["Reply-To"] = "support@saga-xingguang.com"

        html_part = MIMEText(content, "html", "utf-8")
        msg.attach(html_part)

        errs = server.sendmail(sender, to, msg.as_string())
        server.quit()
        if errs:
            print(errs)
            return False
        return True
        
    except Exception as e:
        print(e)
        return False

# 面试邀请  
def compose_interview_email(id, name, dept, time,link):
    content = f"""
  <html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Simple Transactional Email</title>
    <style media="all" type="text/css">
    /* -------------------------------------
    GLOBAL RESETS
------------------------------------- */
    
    body {{
      font-family: Helvetica, sans-serif;
      -webkit-font-smoothing: antialiased;
      font-size: 16px;
      line-height: 1.3;
      -ms-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
      
    }}
    
    table {{      border-collapse: separate;
      /* mso-table-lspace: 0pt;
      mso-table-rspace: 0pt; */
      width: 100%;
    }}
    
    table td {{      
      font-family: Helvetica, sans-serif;
      font-size: 16px;
      vertical-align: top;
    }}
    /* -------------------------------------
    BODY & CONTAINER
------------------------------------- */
    
    body {{      
      background-color:rgb(255,189,89);
      margin: 0;
      padding: 0;
    }}

    .body {{
      width: 100%;
    }}
    .signature-thin{{      margin-top: 3em;
      line-height: 1.3;
      font-size: 12px;
    }}
    .signature-plus {{      margin-top: 2em;
      line-height: 0.4;
      font-style: italic;
    }}
    .highlight {{      font-weight: bold;
      color: #dcac0f;
    }}
    .highlight-thin {{      color: #dcac0f;
      font-style:oblique;
    }}
    .des-post{{        font-size: 14px;
    }} 
    .container {{      margin: 0 auto !important;
      max-width: 600px;
      padding: 0;
      padding-top: 24px;
      width: 600px;
    }}   
    .content {{      box-sizing: border-box;
      display: block;
      margin: 0 auto;
      max-width: 600px;
      padding: 0;
    }}
    /* -------------------------------------
    HEADER, FOOTER, MAIN
------------------------------------- */
    
    .main {{     background: #f6f6e0;
      border: 1px solid #eaebed;
      border-radius: 16px;
      width: 100%;
    }}
    
    .wrapper {{      box-sizing: border-box;
      padding: 24px;
    }}
    
    .footer {{      clear: both;
      padding-top: 24px;
      padding-bottom: 5%;
      text-align: center;
      width: 100%;
    }}
    
    .footer td,
    .footer p,
    .footer span,
    .footer a {{      color: #d37d37;
      font-size: 16px;
      text-align: center;
    }}
    /* -------------------------------------
    TYPOGRAPHY
------------------------------------- */
    
    p {{      font-family: Helvetica, sans-serif;
      font-size: 16px;
      font-weight: normal;
      margin: 0;
      margin-bottom: 16px;
    }}
    a:link{{	
      color: #dcac0f;
    }}
    a:visited{{
      color:rgb(255,167,27);
    }}
    a:hover{{
      color:rgb(255,195,33);
    }}
    a:active{{
      color:rgb(255,141,27);
    }}
    .namestyle{{      font-style: italic;
      font-weight: bold;
      color: #dcac0f;
    }}
    /* -
    OTHER STYLES THAT MIGHT BE USEFUL
------------------------------------- */
    .preheader {{      color: transparent;
      display: none;
      height: 0;
      max-height: 0;
      max-width: 0;
      opacity: 0;
      overflow: hidden;
      /* mso-hide: all; */
      visibility: hidden;
      width: 0;
    }}
    
    .powered-by a {{      text-decoration: none;
    }}
    
    /* -------------------------------------
    RESPONSIVE AND MOBILE FRIENDLY STYLES
------------------------------------- */
    
    @media only screen and (max-width: 640px) {{      .main p,
      .main td,
      .main span {{        font-size: 16px !important;
      }}
      .wrapper {{        padding: 8px !important;
      }}
      .content {{        padding: 0 !important;
      }}
      .container {{        padding: 0 !important;
        padding-top: 8px !important;
        width: 100% !important;
      }}
      .main {{        border-left-width: 0 !important;
        border-radius: 0 !important;
        border-right-width: 0 !important;
      }}
    }}
    /* -------------------------------------
    PRESERVE THESE STYLES IN THE HEAD
------------------------------------- */
    
    @media all {{      .ExternalClass {{        width: 100%;
      }}
      .ExternalClass,
      .ExternalClass p,
      .ExternalClass span,
      .ExternalClass font,
      .ExternalClass td,
      .ExternalClass div {{        line-height: 100%;
      }}
      .apple-link a {{        color: inherit !important;
        font-family: inherit !important;
        font-size: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        text-decoration: none !important;
      }}
      #MessageViewBody a {{        color: inherit;
        text-decoration: none;
        font-size: inherit;
        font-family: inherit;
        font-weight: inherit;
        line-height: inherit;
      }}
    }}
    /* picture */

   .pic-top{{display: flex;
     flex-direction: column;
     text-align: center;
     justify-content: center;
     align-items: center;
     width: 100%;
   }}
   .pic-top img {{      
        width: 100%;
      height: auto;
    }}
   .pic-QR{{       display: flex;
        justify-content: center;
        align-items: center;
   }}
    .pic-QR img {{      
        width: 50%;
    }}
    </style>
  </head>
  <body>
    <div class="pic-top">
      <img src="http://saga-xingguang.com/static/public/imgs/writing-task-email-banner.jpg" alt="">
    </div>
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body">
      <tr>
        <td>&nbsp;</td>
        <td class="container">
          <div class="content">

            <!-- START CENTERED WHITE CONTAINER -->
            <span class="preheader">SAGA星光·第五期 - 面试邀请</span>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="main">

              <!-- START MAIN CONTENT AREA -->
              <tr>
                <td class="wrapper">
                  <p>亲爱的{name}同学,</p>
                  <p>您好!</p>
                  <p>感谢您对志行会SAGA星光线上课堂项目的支持！经{code_to_dept[dept]}评估，您顺利通过笔试。我们诚挚地邀请您参加SAGA星光项目组的面试，以增进彼此了解。</p>
                  <p>以下是面试的详细信息：</p> 
                  <ul>
                    <li>面试时间：<span class="highlight">{time}</span></li>
                    <li>面试平台：腾讯会议</li>
                    <li>会议链接：<span class="highlight">{link}</span></li>
                    <li>面试时长：30-60分钟</li>
                    <li>面试语言：中文</li>
                    <li>服装要求：得体大方</li>                  
                  </ul>
                  <p>如果您无法按照预定时间参加面试或有任何疑问，请在<span class="highlight">24小时内(即{interview_reply_time_ddl}前)</span>回复此邮件与我们联系，我们将尽力安排其他时间或回答您的疑问。（联系方式附后）</p>
                  <br><p>注意事项：</p>
                  <ul>
                    <li>请至少提前五分钟进入腾讯会议以做准备。</li>
                    <li>若迟到十分钟以上将被视为自动放弃。</li>
                    <li>在您进入面试会议后，如上一场面试尚未结束，请在等候室稍候。</li>
                    <li>请确保您的网络连接良好，摄像头及麦克风工作正常。</li>
                    <li>为保证面试的公正，所有面试将被录制并存档，以备查阅。</li>
                    <li>面试内容包括对个人信息、报名岗位的提问，并与笔试内容相关，群体面试会增设小组讨论环节。</li>
                    <li>您可以提前浏览SAGA公众号进行更多了解。（下附二维码）</li>
                  </ul>
                  <div class="pic-QR">
                    <img src="二维码.png" alt="QR code">
                  </div>

                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary" >
                    <tbody>
                      <tr>
                        <td align="left">
                          <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                            <tbody>                             
                            </tbody>           
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <p><br>如果您遇到任何问题，请发送邮件与我们联系。
                  <br>
                  <span class="des-post">技术支持邮箱：</span><span class="highlight-thin">support@saga-xingguang.com</span>
                  <br>
                  <span class="des-post">人事部邮箱：</span><span class="highlight-thin">human-resource@saga-xingguang.com</span>
                  </p>
                  <p>再次感谢您对志行会SAGA星光项目组的关注，祝您好运!</p>
                  <div class="signature-thin">
                    <p>顺颂，<br>夏祺</p>
                  </div>
                  <div class="signature-thin">
                    <p>志行会SAGA星光项目组·{{code_to_dept[dept]}}敬上</p>
                    <p>---SAGA星光团队 </p>
                  </div>
                  
                </td>
              </tr>

              <!-- END MAIN CONTENT AREA -->
              </table>

            <!-- START FOOTER -->
            <div class="footer">
              <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                <tr>
                  <td class="content-block">
                    <span style="font-weight: bold;">SAGA·星光</span>
                    <br>
                  </td>
                </tr>
                <tr>
                  <!-- <td class="content-block powered-by">
                    Powered by <a href="http://htmlemail.io">HTMLemail.io</a>
                  </td> -->
                </tr>
              </table>
            </div>

            <!-- END FOOTER -->
            
<!-- END CENTERED WHITE CONTAINER --></div>
        </td>
        <td>&nbsp;</td>
      </tr>
    </table>
    
  </body>
</html>
"""
    return content


def send_interview_email_with_support(to, subject, content) -> bool:
    try:
        sender = "support@saga-xingguang.com"
        server = smtplib.SMTP('smtp.feishu.cn', 587)
        server.starttls()
        server.login(sender, os.environ.get("SAGA_HR_EMAIL_PASSWORD", ""))
        
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "【SAGA】2024-2025年度志愿者招募面试邀请函"
        msg["From"] = sender
        msg["To"] = to
        msg["Reply-To"] = "support@saga-xingguang.com"

        html_part = MIMEText(content, "html", "utf-8")
        msg.attach(html_part)

        errs = server.sendmail(sender, to, msg.as_string())
        server.quit()
        if errs:
            print(errs)
            return False
        return True
        
    except Exception as e:
        print(e)
        return False

# 发送offer
def compose_accept_email(id, name, dept, offer_reply_ddl):
    eng=dept_to_eng.get(dept)
    content = f"""
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Simple Transactional Email</title>
    <style media="all" type="text/css">
    /* -------------------------------------
    GLOBAL RESETS
------------------------------------- */
    
    body {{
      font-family: Helvetica, sans-serif;
      -webkit-font-smoothing: antialiased;
      font-size: 16px;
      line-height: 1.3;
      -ms-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
      
    }}
    
    table {{      border-collapse: separate;
      /* mso-table-lspace: 0pt;
      mso-table-rspace: 0pt; */
      width: 100%;
    }}
    
    table td {{      font-family: Helvetica, sans-serif;
      font-size: 16px;
      vertical-align: top;
    }}
    /* -------------------------------------
    BODY & CONTAINER
------------------------------------- */
    
    body {{      background-color:rgb(255,189,89);
      margin: 0;
      padding: 0;
    }}

    .body {{
      width: 100%;
    }}
    .signature-thin{{      margin-top: 3em;
      line-height: 1.3;
      font-size: 12px;
    }}
    .signature-plus {{      margin-top: 2em;
      line-height: 0.4;
      font-style: italic;
    }}
    .highlight {{      font-weight: bold;
      color: #dcac0f;
    }}
    .highlight-thin {{      color: #dcac0f;
      font-style:oblique;
    }}
    .des-post{{        font-size: 14px;
    }} 
    .container {{      margin: 0 auto !important;
      max-width: 600px;
      padding: 0;
      padding-top: 24px;
      width: 600px;
    }}
    
    .content {{      box-sizing: border-box;
      display: block;
      margin: 0 auto;
      max-width: 600px;
      padding: 0;
    }}
    /* -------------------------------------
    HEADER, FOOTER, MAIN
------------------------------------- */
    
    .main {{      background: #f6f6e0;
      border: 1px solid #eaebed;
      border-radius: 16px;
      width: 100%;
    }}
    
    .wrapper {{      box-sizing: border-box;
      padding: 24px;
    }}
    
    .footer {{      clear: both;
      padding-top: 24px;
      padding-bottom: 5%;
      text-align: center;
      width: 100%;
    }}
    
    .footer td,
    .footer p,
    .footer span,
    .footer a {{      color: #d37d37;
      font-size: 16px;
      text-align: center;
    }}
    /* -------------------------------------
    TYPOGRAPHY
------------------------------------- */
    
    p {{      font-family: Helvetica, sans-serif;
      font-size: 16px;
      font-weight: normal;
      margin: 0;
      margin-bottom: 16px;
    }}
    a:link{{	/*默认状态*/
      color: #dcac0f;
    }}
    a:visited{{/*浏览过的*/
      color:rgb(255,167,27);
    }}
    a:hover{{/*悬浮状态*/
      color:rgb(255,195,33);
    }}
    a:active{{/*激活过的*/
      color:rgb(255,141,27);
    }}
    .namestyle{{      font-style: italic;
      font-weight: bold;
      color: #dcac0f;
    }}
    /* -
    OTHER STYLES THAT MIGHT BE USEFUL
------------------------------------- */
    .preheader {{      color: transparent;
      display: none;
      height: 0;
      max-height: 0;
      max-width: 0;
      opacity: 0;
      overflow: hidden;
      /* mso-hide: all; */
      visibility: hidden;
      width: 0;
    }}
    
    .powered-by a {{      text-decoration: none;
    }}
    
    /* -------------------------------------
    RESPONSIVE AND MOBILE FRIENDLY STYLES
------------------------------------- */
    
    @media only screen and (max-width: 640px) {{      .main p,
      .main td,
      .main span {{        font-size: 16px !important;
      }}
      .wrapper {{        padding: 8px !important;
      }}
      .content {{        padding: 0 !important;
      }}
      .container {{        padding: 0 !important;
        padding-top: 8px !important;
        width: 100% !important;
      }}
      .main {{        border-left-width: 0 !important;
        border-radius: 0 !important;
        border-right-width: 0 !important;
      }}
    }}
    /* -------------------------------------
    PRESERVE THESE STYLES IN THE HEAD
------------------------------------- */
    
    @media all {{      .ExternalClass {{        width: 100%;
      }}
      .ExternalClass,
      .ExternalClass p,
      .ExternalClass span,
      .ExternalClass font,
      .ExternalClass td,
      .ExternalClass div {{        line-height: 100%;
      }}
      .apple-link a {{        color: inherit !important;
        font-family: inherit !important;
        font-size: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        text-decoration: none !important;
      }}
      #MessageViewBody a {{        color: inherit;
        text-decoration: none;
        font-size: inherit;
        font-family: inherit;
        font-weight: inherit;
        line-height: inherit;
      }}
    }}
    /* picture */

   .pic-top{{      display: flex;
     flex-direction: column;
     text-align: center;
     justify-content: center;
     align-items: center;
     width: 100%;
   }}
   .pic-top img {{      
        width: 100%;
      height: auto;
    }}
   
    .pic-QR{{    display: flex;
        justify-content: center;
        align-items: center;
   }}
    .pic-QR img {{     
        width: 90%;
    }}

    </style>
  </head>
  <body>
    <div class="pic-top">
      <img src="http://saga-xingguang.com/static/public/imgs/writing-task-email-banner.jpg" alt="">
    </div>
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body">
      <tr>
        <td>&nbsp;</td>
        <td class="container">
          <div class="content">
            <span class="preheader">SAGA星光·第五期 - 录取通知</span>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="main">

              <!-- START MAIN CONTENT AREA -->
              <tr>
                <td class="wrapper">
                  <p>亲爱的{name}同学,</p>
                  <p>您好!</p>
                  <p>感谢您参加志行会星光线上课堂项目组的招募，鉴于您对公益的热情与您在面试中出众的表现，星光项目组诚挚邀请您成为我们的一员，与所有BTPer一起为我们共同的公益梦想努力。</p> 
                  
                  <p>您的具体职位是<span style="font-weight: bold;">{code_to_dept[dept]}成员</span>。</p>
                  <p>请扫描<a href="https://lcny1jsoyn29.feishu.cn/wiki/E0BmwziX0inqrPkrjjYc5JvjnXc";>此链接</a>中的二维码，加入到SAGA的飞书团队及微信群，SAGA所有数据都储存在飞书内，主要工作也将在飞书开展，<span class="highlight">请务必保证加入以免消息遗漏</span>。</p>
    
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary" >
                    <tbody>
                      <tr>
                        <td align="left">
                          <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                            <tbody>                             
                            </tbody>           
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <p><br>请您在看到本录取通知后尽快回复邮件表明您是否接受录取，我们在您接受offer后将在飞书通知后续安排。如在<span class="highlight-thin">{offer_reply_ddl}</span>前我们仍没有接到您的回复，我们将视为您自动放弃该职位。
                  <br>
                  
                  <p>再次感谢您对志行会星光项目组的支持与关注！</p>
                  <div class="signature-thin">
                    <p>顺颂，<br>夏祺</p>
                  </div>
                  <div class="signature-thin">
                    <p>志行会SAGA星光项目组 敬上</p>
                  </div><br><hr>
                  <p>Dear candidate,</p>
                  <p>Thank you for participating in the recruitment of BTP-SAGA. Due to your enthusiasm for public welfare and outstanding performance during the interview, we are glad to offer you as a member of BTP-SAGA. We hope that you can strive after our mutual public welfare dreams with all BTPers!</p>
                  <p>Your position is a member of <span style="font-weight: bold;">{code_to_dept[dept]} Department</p> 
                  
                  <p>Please scan the <a href="https://lcny1jsoyn29.feishu.cn/wiki/E0BmwziX0inqrPkrjjYc5JvjnXc">QR codes</a> to enter our Lark Team and WeChat group. All documents of BTP-SAGA are saved in Lark for your reference, and we will carry out our main tasks through it as well. Please join them once you decide to accept the offer. </p>
                  <p>Please reply to this email as soon as possible to confirm your acceptanc. After you accept the offer, we will notify you through Lark for further arrangement. Kindly note that if we do not receive your reply before <span class="highlight-thin">{offer_reply_ddl}</span>, we will assume that you have automatically given up the position.</p>

                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary" >
                    <tbody>
                      <tr>
                        <td align="left">
                          <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                            <tbody>                             
                            </tbody>           
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <p>Again, thank you for keeping up with BTP SAGA.</p>
                  <p>Best Regards,</p>
                  <p>BTP-SAGA</p>
                  
                </td>
              </tr>
              <!-- END MAIN CONTENT AREA -->
              </table>

            <!-- START FOOTER -->
            <div class="footer">
              <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                <tr>
                  <td class="content-block">
                    <span class="apple-link">微信公众号：星光SAGA</span>
                    <br>
                    <span class="apple-link">联系邮箱：support@saga-xingguang.com</span>
                    <br>
                    
                  </td>
                </tr>
                <tr>
                </tr>
              </table>
            </div>

            <!-- END FOOTER -->
            
<!-- END CENTERED WHITE CONTAINER --></div>
        </td>
        <td>&nbsp;</td>
      </tr>
    </table>
    
  </body>
</html>
"""
    return content


def send_offer_email_with_hr(to, subject, content) -> bool:
    try:
        sender = "human-resource@saga-xingguang.com"
        server = smtplib.SMTP('smtp.feishu.cn', 587)
        server.starttls()
        server.login(sender, os.environ.get("SAGA_HR_EMAIL_PASSWORD", ""))
        
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "【SAGA】2024-2025年度志愿者招募结果"
        msg["From"] = sender
        msg["To"] = to
        msg["Reply-To"] = "human-resource@saga-xingguang.com"

        html_part = MIMEText(content, "html", "utf-8")
        msg.attach(html_part)

        errs = server.sendmail(sender, to, msg.as_string())
        server.quit()
        if errs:
            print(errs)
            return False
        return True
        
    except Exception as e:
        print(e)
        return False

# reject
def compose_reject_email(id, name, dept):
    eng=dept_to_eng.get(dept)
    content = f"""
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Simple Transactional Email</title>
    <style media="all" type="text/css">
    /* -------------------------------------
    GLOBAL RESETS
------------------------------------- */
    
    body {{
      font-family: Helvetica, sans-serif;
      -webkit-font-smoothing: antialiased;
      font-size: 16px;
      line-height: 1.3;
      -ms-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
      
    }}
    
    table {{      border-collapse: separate;
      /* mso-table-lspace: 0pt;
      mso-table-rspace: 0pt; */
      width: 100%;
    }}
    
    table td {{      font-family: Helvetica, sans-serif;
      font-size: 16px;
      vertical-align: top;
    }}
    /* -------------------------------------
    BODY & CONTAINER
------------------------------------- */
    
    body {{      background-color:rgb(255,189,89);
      margin: 0;
      padding: 0;
    }}

    .body {{
      width: 100%;
    }}
    .signature-thin{{      margin-top: 3em;
      line-height: 1.3;
      font-size: 12px;
    }}
    .signature-plus {{      margin-top: 2em;
      line-height: 0.4;
      font-style: italic;
    }}
    .highlight {{      font-weight: bold;
      color: #dcac0f;
    }}
    .highlight-thin {{      color: #dcac0f;
      font-style:oblique;
    }}
    .des-post{{        font-size: 14px;
    }} 
    .container {{      margin: 0 auto !important;
      max-width: 600px;
      padding: 0;
      padding-top: 24px;
      width: 600px;
    }}
    .content {{      box-sizing: border-box;
      display: block;
      margin: 0 auto;
      max-width: 600px;
      padding: 0;
    }}
    /* -------------------------------------
    HEADER, FOOTER, MAIN
------------------------------------- */
    
    .main {{      background: #f6f6e0;
      border: 1px solid #eaebed;
      border-radius: 16px;
      width: 100%;
    }}
    
    .wrapper {{      box-sizing: border-box;
      padding: 24px;
    }}
    
    .footer {{      clear: both;
      padding-top: 24px;
      padding-bottom: 5%;
      text-align: center;
      width: 100%;
    }}
    
    .footer td,
    .footer p,
    .footer span,
    .footer a {{      color: #d37d37;
      font-size: 16px;
      text-align: center;
    }}
    /* -------------------------------------
    TYPOGRAPHY
------------------------------------- */
    
    p {{      font-family: Helvetica, sans-serif;
      font-size: 16px;
      font-weight: normal;
      margin: 0;
      margin-bottom: 16px;
    }}
    a:link{{	/*默认状态*/
      color: #dcac0f;
    }}
    a:visited{{/*浏览过的*/
      color:rgb(255,167,27);
    }}
    a:hover{{/*悬浮状态*/
      color:rgb(255,195,33);
    }}
    a:active{{/*激活过的*/
      color:rgb(255,141,27);
    }}
    .namestyle{{      font-style: italic;
      font-weight: bold;
      color: #dcac0f;
    }}
    /* -
    OTHER STYLES THAT MIGHT BE USEFUL
------------------------------------- */
    .preheader {{      color: transparent;
      display: none;
      height: 0;
      max-height: 0;
      max-width: 0;
      opacity: 0;
      overflow: hidden;
      /* mso-hide: all; */
      visibility: hidden;
      width: 0;
    }}
    
    .powered-by a {{      text-decoration: none;
    }}
    
    /* -------------------------------------
    RESPONSIVE AND MOBILE FRIENDLY STYLES
------------------------------------- */
    
    @media only screen and (max-width: 640px) {{      .main p,
      .main td,
      .main span {{        font-size: 16px !important;
      }}
      .wrapper {{        padding: 8px !important;
      }}
      .content {{        padding: 0 !important;
      }}
      .container {{        padding: 0 !important;
        padding-top: 8px !important;
        width: 100% !important;
      }}
      .main {{        border-left-width: 0 !important;
        border-radius: 0 !important;
        border-right-width: 0 !important;
      }}
    }}
    /* -------------------------------------
    PRESERVE THESE STYLES IN THE HEAD
------------------------------------- */
    
    @media all {{      .ExternalClass {{        width: 100%;
      }}
      .ExternalClass,
      .ExternalClass p,
      .ExternalClass span,
      .ExternalClass font,
      .ExternalClass td,
      .ExternalClass div {{        line-height: 100%;
      }}
      .apple-link a {{        color: inherit !important;
        font-family: inherit !important;
        font-size: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        text-decoration: none !important;
      }}
      #MessageViewBody a {{        color: inherit;
        text-decoration: none;
        font-size: inherit;
        font-family: inherit;
        font-weight: inherit;
        line-height: inherit;
      }}
    }}
    /* picture */

   .pic-top{{      display: flex;
     flex-direction: column;
     text-align: center;
     justify-content: center;
     align-items: center;
     width: 100%;
   }}
   .pic-top img {{      
        width: 100%;
      height: auto;
    }}
    </style>
  </head>
  <body>
    <div class="pic-top">
      <img src="http://saga-xingguang.com/static/public/imgs/writing-task-email-banner.jpg" alt="">
    </div>
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body">
      <tr>
        <td>&nbsp;</td>
        <td class="container">
          <div class="content">

            <!-- START CENTERED WHITE CONTAINER -->
            <span class="preheader">SAGA星光·第五期 - 录取通知</span>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="main">

              <!-- START MAIN CONTENT AREA -->
              <tr>
                <td class="wrapper">
                  <p>亲爱的{name}同学,</p>
                  <p>您好!</p>
                  <p>感谢您参加志行会SAGA星光线上课堂项目组{code_to_dept[dept]}的招募以及对星光公益课堂的关注和支持，我们很遗憾的通知您没有通过本次招募。</p>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary" >
                    <tbody>
                      <tr>
                        <td align="left">
                          <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                            <tbody>                             
                            </tbody>           
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <p>我们非常认可您的热情和爱心，在申请审核过程中，我们严格按照招募条件和要求对每一位申请人进行评估，但由于竞争过于激烈，我们无法收纳所有的申请者。</p>
                  <p>请不要因此感到失望，无论结果如何，我们仍然非常赞赏您对公益事业的热情和支持。我们也相信您一定会找到更适合自己地方，更相信您未来所处的地方会因为您的加入而获益无穷。</p>
                  <p>再次感谢您对志行会SAGA星光项目组的关注！</p>
                  <div class="signature-thin">
                    <p>顺颂，<br>夏祺</p>
                  </div>
                  <div class="signature-thin">
                    <p>志行会SAGA星光项目组 敬上</p>
                  </div><br>
                  <hr>
                  <p>Dear candidate,</p>
                  <p>Thank you for your participation in the recruitment of the BTP-SAGA Project {code_to_dept[dept]} Department and your interest and support for BTP-SAGA. We regret to inform you that you did not pass this test.</p> 
                  <p>We appreciate your enthusiasm and compassion. During the application review process, we evaluated each applicant in strict accordance with the recruitment conditions and requirements, but unfortunately, due to overwhelming competition, we were unable to accept all applicants.</p>
                  <p>Please do not be discouraged by this decision. We value your enthusiasm and commitment to public welfare, and we encourage you to continue following our activities and projects. We hope that future opportunities will arise for you to join us in our mission.</p>
                  <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary" >
                    <tbody>
                      <tr>
                        <td align="left">
                          <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                            <tbody>                             
                            </tbody>           
                          </table>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <p>Thank you again for your interest in BTP-SAGA. We wish you all the best in your future endeavors.</p>
                  <p>Best Regards,</p>
                  <p>BTP-SAGA</p>
                  
                </td>
              </tr>
              <!-- END MAIN CONTENT AREA -->
              </table>

            <!-- START FOOTER -->
            <div class="footer">
              <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                <tr>
                  <td class="content-block">
                    <span class="apple-link">微信公众号：星光SAGA</span>
                    <br>
                    <span class="apple-link">联系邮箱：support@saga-xingguang.com</span>
                    <br>
                    
                  </td>
                </tr>
                <tr>
                  <!-- <td class="content-block powered-by">
                    Powered by <a href="http://htmlemail.io">HTMLemail.io</a>
                  </td> -->
                </tr>
              </table>
            </div>

            <!-- END FOOTER -->
            
<!-- END CENTERED WHITE CONTAINER --></div>
        </td>
        <td>&nbsp;</td>
      </tr>
    </table>
    
  </body>
</html>
"""
    return content


def send_reject_email_with_hr(to, subject, content) -> bool:
    try:
        sender = "human-resource@saga-xingguang.com"
        server = smtplib.SMTP('smtp.feishu.cn', 587)
        server.starttls()
        server.login(sender, os.environ.get("SAGA_HR_EMAIL_PASSWORD", ""))
        
        msg = MIMEMultipart("alternative")
        msg["Subject"] = "【SAGA】2024-2025年度志愿者招募结果"
        msg["From"] = sender
        msg["To"] = to
        msg["Reply-To"] = "human-resource@saga-xingguang.com"

        html_part = MIMEText(content, "html", "utf-8")
        msg.attach(html_part)

        errs = server.sendmail(sender, to, msg.as_string())
        server.quit()
        if errs:
            print(errs)
            return False
        return True
        
    except Exception as e:
        print(e)
        return False
