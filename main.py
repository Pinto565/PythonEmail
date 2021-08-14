import pandas as pd
import smtplib
from email.message import EmailMessage

html_content = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html
  xmlns="http://www.w3.org/1999/xhtml"
  xmlns:o="urn:schemas-microsoft-com:office:office"
  style="
    width: 100%;
    font-family: 'Open Sans', sans-serif;
    -webkit-text-size-adjust: 100%;
    -ms-text-size-adjust: 100%;
    padding: 0;
    margin: 0;
  "
>
  <head>
    <meta charset="UTF-8" />
    <meta content="width=device-width, initial-scale=1" name="viewport" />
    <meta name="x-apple-disable-message-reformatting" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta content="telephone=no" name="format-detection" />
    <title>New Template</title>
    <!--[if (mso 16)
      ]><style type="text/css">
        a {
          text-decoration: none;
        }
      </style><!
    [endif]-->
    <!--[if gte mso 9
      ]><style>
        sup {
          font-size: 100% !important;
        }
      </style><!
    [endif]-->
    <!--[if gte mso 9
      ]><xml>
        <o:OfficeDocumentSettings>
          <o:AllowPNG></o:AllowPNG> <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
      </xml><!
    [endif]-->
    <style type="text/css">
      #outlook a {
        padding: 0;
      }

      .ExternalClass {
        width: 100%;
      }

      .ExternalClass,
      .ExternalClass p,
      .ExternalClass span,
      .ExternalClass font,
      .ExternalClass td,
      .ExternalClass div {
        line-height: 100%;
      }

      .es-button {
        mso-style-priority: 100 !important;
        text-decoration: none !important;
      }

      a[x-apple-data-detectors] {
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
      }

      .es-desk-hidden {
        display: none;
        float: left;
        overflow: hidden;
        width: 0;
        max-height: 0;
        line-height: 0;
        mso-hide: all;
      }

      @media only screen and (max-width: 600px) {
        p,
        ul li,
        ol li,
        a {
          font-size: 14px !important;
          line-height: 150% !important;
        }

        h1 {
          font-size: 28px !important;
          text-align: left;
          line-height: 120%;
        }

        h2 {
          font-size: 20px !important;
          text-align: left;
          line-height: 120%;
        }

        h3 {
          font-size: 14px !important;
          text-align: left;
          line-height: 120%;
        }

        h1 a {
          font-size: 28px !important;
          text-align: left;
        }

        h2 a {
          font-size: 20px !important;
          text-align: left;
        }

        h3 a {
          font-size: 14px !important;
          text-align: left;
        }

        .es-menu td a {
          font-size: 14px !important;
        }

        .es-header-body p,
        .es-header-body ul li,
        .es-header-body ol li,
        .es-header-body a {
          font-size: 14px !important;
        }

        .es-footer-body p,
        .es-footer-body ul li,
        .es-footer-body ol li,
        .es-footer-body a {
          font-size: 14px !important;
        }

        .es-infoblock p,
        .es-infoblock ul li,
        .es-infoblock ol li,
        .es-infoblock a {
          font-size: 14px !important;
        }

        *[class="gmail-fix"] {
          display: none !important;
        }

        .es-m-txt-c,
        .es-m-txt-c h1,
        .es-m-txt-c h2,
        .es-m-txt-c h3 {
          text-align: center !important;
        }

        .es-m-txt-r,
        .es-m-txt-r h1,
        .es-m-txt-r h2,
        .es-m-txt-r h3 {
          text-align: right !important;
        }

        .es-m-txt-l,
        .es-m-txt-l h1,
        .es-m-txt-l h2,
        .es-m-txt-l h3 {
          text-align: left !important;
        }

        .es-m-txt-r img,
        .es-m-txt-c img,
        .es-m-txt-l img {
          display: inline !important;
        }

        .es-button-border {
          display: block !important;
        }

        .es-btn-fw {
          border-width: 10px 0px !important;
          text-align: center !important;
        }

        .es-adaptive table,
        .es-btn-fw,
        .es-btn-fw-brdr,
        .es-left,
        .es-right {
          width: 100% !important;
        }

        .es-content table,
        .es-header table,
        .es-footer table,
        .es-content,
        .es-footer,
        .es-header {
          width: 100% !important;
          max-width: 600px !important;
        }

        .es-adapt-td {
          display: block !important;
          width: 100% !important;
        }

        .adapt-img {
          width: 100% !important;
          height: auto !important;
        }

        .es-m-p0 {
          padding: 0px !important;
        }

        .es-m-p0r {
          padding-right: 0px !important;
        }

        .es-m-p0l {
          padding-left: 0px !important;
        }

        .es-m-p0t {
          padding-top: 0px !important;
        }

        .es-m-p0b {
          padding-bottom: 0 !important;
        }

        .es-m-p20b {
          padding-bottom: 20px !important;
        }

        .es-mobile-hidden,
        .es-hidden {
          display: none !important;
        }

        tr.es-desk-hidden,
        td.es-desk-hidden,
        table.es-desk-hidden {
          width: auto !important;
          overflow: visible !important;
          float: none !important;
          max-height: inherit !important;
          line-height: inherit !important;
        }

        tr.es-desk-hidden {
          display: table-row !important;
        }

        table.es-desk-hidden {
          display: table !important;
        }

        td.es-desk-menu-hidden {
          display: table-cell !important;
        }

        table.es-table-not-adapt,
        .esd-block-html table {
          width: auto !important;
        }

        table.es-social {
          display: inline-block !important;
        }

        table.es-social td {
          display: inline-block !important;
        }

        a.es-button,
        button.es-button {
          font-size: 14px !important;
          display: block !important;
          border-bottom-width: 20px !important;
          border-right-width: 0px !important;
          border-left-width: 0px !important;
        }
      }
    </style>
    <!--[if !mso]><!-- -->
    <link
      href="https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700,700i"
      rel="stylesheet"
    />
    <link
      href="https://fonts.googleapis.com/css?family=Roboto:400,400i,700,700i"
      rel="stylesheet"
    />
    <!--<![endif]-->
  </head>

  <body
    style="
      width: 100%;
      font-family: 'Open Sans', sans-serif;
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
      padding: 0;
      margin: 0;
    "
  >
    <div class="es-wrapper-color" style="background-color: #04070c">
      <!--[if gte mso 9
        ]><v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
          <v:fill
            type="tile"
            color="#04070c"
            origin="0.5, 0"
            position="0.5,0"
          ></v:fill> </v:background
      ><![endif]-->
      <table
        class="es-wrapper"
        width="100%"
        cellspacing="0"
        cellpadding="0"
        style="
          mso-table-lspace: 0pt;
          mso-table-rspace: 0pt;
          border-collapse: collapse;
          border-spacing: 0px;
          padding: 0;
          margin: 0;
          width: 100%;
          height: 100%;
          background-repeat: repeat;
          background-position: center top;
        "
      >
        <tbody>
          <tr style="border-collapse: collapse">
            <td valign="top" style="padding: 0; margin: 0">
              <table
                class="es-header"
                cellspacing="0"
                cellpadding="0"
                align="center"
                style="
                  mso-table-lspace: 0pt;
                  mso-table-rspace: 0pt;
                  border-collapse: collapse;
                  border-spacing: 0px;
                  table-layout: fixed !important;
                  width: 100%;
                  background-color: #333333;
                  background-repeat: repeat;
                  background-position: center top;
                "
              >
                <tbody>
                  <tr style="border-collapse: collapse">
                    <td
                      align="center"
                      bgcolor="#fbd80d"
                      style="padding: 0; margin: 0; background-color: #fbd80d"
                    >
                      <table
                        class="es-header-body"
                        cellspacing="0"
                        cellpadding="0"
                        bgcolor="#000001"
                        align="center"
                        style="
                          mso-table-lspace: 0pt;
                          mso-table-rspace: 0pt;
                          border-collapse: collapse;
                          border-spacing: 0px;
                          background-color: #000001;
                          width: 600px;
                        "
                      >
                        <tbody>
                          <tr style="border-collapse: collapse">
                            <td
                              align="left"
                              style="
                                margin: 0;
                                padding-left: 15px;
                                padding-right: 15px;
                                padding-top: 20px;
                                padding-bottom: 20px;
                              "
                            >
                              <table
                                cellspacing="0"
                                cellpadding="0"
                                width="100%"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tbody>
                                  <tr style="border-collapse: collapse">
                                    <td
                                      class="es-m-p0r"
                                      valign="top"
                                      align="center"
                                      style="
                                        padding: 0;
                                        margin: 0;
                                        width: 570px;
                                      "
                                    >
                                      <table
                                        width="100%"
                                        cellspacing="0"
                                        cellpadding="0"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          border-collapse: collapse;
                                          border-spacing: 0px;
                                        "
                                      >
                                        <tbody>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="center"
                                              class="es-m-txt-c"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                font-size: 0px;
                                              "
                                            >
                                              <a
                                                target="_blank"
                                                href="https://www.pattarai.in/"
                                                style="
                                                  -webkit-text-size-adjust: none;
                                                  -ms-text-size-adjust: none;
                                                  mso-line-height-rule: exactly;
                                                  font-family: 'Open Sans',
                                                    sans-serif;
                                                  font-size: 12px;
                                                  text-decoration: none;
                                                  color: #ffffff;
                                                "
                                                ><img
                                                  src="https://oiyomk.stripocdn.email/content/guids/CABINET_0df4df06df1e292624be9e46022c3657/images/6391606026932137.png"
                                                  alt="Pattarai"
                                                  style="
                                                    display: block;
                                                    border: 0;
                                                    outline: none;
                                                    text-decoration: none;
                                                    -ms-interpolation-mode: bicubic;
                                                  "
                                                  width="255"
                                                  title="Pattarai"
                                              /></a>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                          <tr style="border-collapse: collapse">
                            <td align="left" style="padding: 0; margin: 0">
                              <table
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tbody>
                                  <tr style="border-collapse: collapse">
                                    <td
                                      align="center"
                                      valign="top"
                                      style="
                                        padding: 0;
                                        margin: 0;
                                        width: 600px;
                                      "
                                    >
                                      <table
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          border-collapse: collapse;
                                          border-spacing: 0px;
                                        "
                                      >
                                        <tbody>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="center"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                font-size: 0px;
                                              "
                                            >
                                              <a
                                                target="_blank"
                                                href="https://www.pattarai.in/"
                                                style="
                                                  -webkit-text-size-adjust: none;
                                                  -ms-text-size-adjust: none;
                                                  mso-line-height-rule: exactly;
                                                  font-family: 'Open Sans',
                                                    sans-serif;
                                                  font-size: 12px;
                                                  text-decoration: none;
                                                  color: #ffffff;
                                                "
                                                ><img
                                                  class="adapt-img"
                                                  src="https://oiyomk.stripocdn.email/content/guids/CABINET_0df4df06df1e292624be9e46022c3657/images/24901606027130689.jpeg"
                                                  alt
                                                  style="
                                                    display: block;
                                                    border: 0;
                                                    outline: none;
                                                    text-decoration: none;
                                                    -ms-interpolation-mode: bicubic;
                                                  "
                                                  width="600"
                                              /></a>
                                            </td>
                                          </tr>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="center"
                                              class="es-m-txt-c"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                padding-left: 5px;
                                                padding-right: 5px;
                                                padding-top: 20px;
                                              "
                                            >
                                              <h3
                                                style="
                                                  margin: 0;
                                                  line-height: 24px;
                                                  mso-line-height-rule: exactly;
                                                  font-family: roboto,
                                                    'helvetica neue', helvetica,
                                                    arial, sans-serif;
                                                  font-size: 16px;
                                                  font-style: normal;
                                                  font-weight: bold;
                                                  color: #fbfafa;
                                                  letter-spacing: 0px;
                                                "
                                              >
                                                We are proud to present you
                                                Pattarai's very own
                                                newsletter.<br />Here you go!
                                                The first issue of&nbsp;
                                              </h3>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                          <tr style="border-collapse: collapse">
                            <td
                              align="left"
                              bgcolor="transparent"
                              style="
                                margin: 0;
                                padding-left: 15px;
                                padding-right: 15px;
                                padding-top: 20px;
                                padding-bottom: 20px;
                                background-color: transparent;
                              "
                            >
                              <table
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tbody>
                                  <tr style="border-collapse: collapse">
                                    <td
                                      align="center"
                                      valign="top"
                                      style="
                                        padding: 0;
                                        margin: 0;
                                        width: 570px;
                                      "
                                    >
                                      <table
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          border-collapse: collapse;
                                          border-spacing: 0px;
                                        "
                                      >
                                        <tbody>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="center"
                                              class="es-m-txt-c"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                padding-bottom: 5px;
                                              "
                                            >
                                              <h1
                                                style="
                                                  margin: 0;
                                                  line-height: 31px;
                                                  mso-line-height-rule: exactly;
                                                  font-family: roboto,
                                                    'helvetica neue', helvetica,
                                                    arial, sans-serif;
                                                  font-size: 26px;
                                                  font-style: normal;
                                                  font-weight: bold;
                                                  color: #fbd80d;
                                                "
                                              >
                                                <strong>elevate^now</strong>
                                              </h1>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </tbody>
              </table>
              <table
                class="es-content"
                cellspacing="0"
                cellpadding="0"
                align="center"
                style="
                  mso-table-lspace: 0pt;
                  mso-table-rspace: 0pt;
                  border-collapse: collapse;
                  border-spacing: 0px;
                  table-layout: fixed !important;
                  width: 100%;
                "
              >
                <tbody>
                  <tr style="border-collapse: collapse">
                    <td align="center" style="padding: 0; margin: 0">
                      <table
                        class="es-content-body"
                        cellspacing="0"
                        cellpadding="0"
                        bgcolor="#ffffff"
                        align="center"
                        style="
                          mso-table-lspace: 0pt;
                          mso-table-rspace: 0pt;
                          border-collapse: collapse;
                          border-spacing: 0px;
                          background-color: #ffffff;
                          width: 600px;
                        "
                      >
                        <tbody>
                          <tr style="border-collapse: collapse">
                            <td
                              align="left"
                              style="
                                padding: 0;
                                margin: 0;
                                padding-left: 15px;
                                padding-right: 15px;
                                padding-top: 20px;
                              "
                            >
                              <!--[if mso]><table style="width:570px" cellpadding="0" cellspacing="0"><tr><td style="width:285px" valign="top"><![endif]-->
                              <table
                                cellspacing="0"
                                cellpadding="0"
                                align="left"
                                class="es-left"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                  float: left;
                                "
                              >
                                <tbody>
                                  <tr style="border-collapse: collapse">
                                    <td
                                      class="es-m-p20b"
                                      valign="top"
                                      align="center"
                                      style="
                                        padding: 0;
                                        margin: 0;
                                        width: 285px;
                                      "
                                    >
                                      <table
                                        width="100%"
                                        cellspacing="0"
                                        cellpadding="0"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          border-collapse: collapse;
                                          border-spacing: 0px;
                                        "
                                      >
                                        <tbody>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="center"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                font-size: 0px;
                                              "
                                            >
                                              <a
                                                target="_blank"
                                                href="https://www.flipsnack.com/659AF9CC5A8/elevate-now_issue01.html"
                                                style="
                                                  -webkit-text-size-adjust: none;
                                                  -ms-text-size-adjust: none;
                                                  mso-line-height-rule: exactly;
                                                  font-family: 'Open Sans',
                                                    sans-serif;
                                                  font-size: 14px;
                                                  text-decoration: none;
                                                  color: #aeaeaf;
                                                "
                                                ><img
                                                  class="adapt-img b_image"
                                                  src="https://oiyomk.stripocdn.email/content/guids/CABINET_0df4df06df1e292624be9e46022c3657/images/80781606027312870.jpg"
                                                  alt="elevate^now"
                                                  style="
                                                    display: block;
                                                    border: 0;
                                                    outline: none;
                                                    text-decoration: none;
                                                    -ms-interpolation-mode: bicubic;
                                                  "
                                                  width="285"
                                                  title="elevate^now"
                                              /></a>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <!--[if mso]></td><td style="width:20px"></td>
<td style="width:265px" valign="top"><![endif]-->
                              <table
                                cellpadding="0"
                                cellspacing="0"
                                class="es-right"
                                align="right"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                  float: right;
                                "
                              >
                                <tbody>
                                  <tr style="border-collapse: collapse">
                                    <td
                                      valign="top"
                                      align="center"
                                      style="
                                        padding: 0;
                                        margin: 0;
                                        width: 265px;
                                      "
                                    >
                                      <table
                                        width="100%"
                                        cellspacing="0"
                                        cellpadding="0"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          border-collapse: collapse;
                                          border-spacing: 0px;
                                        "
                                      >
                                        <tbody>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="left"
                                              class="es-m-txt-l"
                                              style="padding: 0; margin: 0"
                                            >
                                              <h3
                                                style="
                                                  margin: 0;
                                                  line-height: 19px;
                                                  mso-line-height-rule: exactly;
                                                  font-family: roboto,
                                                    'helvetica neue', helvetica,
                                                    arial, sans-serif;
                                                  font-size: 16px;
                                                  font-style: normal;
                                                  font-weight: bold;
                                                  color: #999999;
                                                  letter-spacing: 0px;
                                                "
                                                class="b_category"
                                              >
                                                POSTED ON NOV 23, 2020
                                              </h3>
                                            </td>
                                          </tr>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="left"
                                              class="es-m-txt-l"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                padding-bottom: 10px;
                                              "
                                            >
                                              <h1
                                                class="b_title"
                                                style="
                                                  margin: 0;
                                                  line-height: 31px;
                                                  mso-line-height-rule: exactly;
                                                  font-family: roboto,
                                                    'helvetica neue', helvetica,
                                                    arial, sans-serif;
                                                  font-size: 26px;
                                                  font-style: normal;
                                                  font-weight: bold;
                                                  color: #3c4858;
                                                "
                                              >
                                                Pattarai's Newsletter
                                              </h1>
                                            </td>
                                          </tr>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="left"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                padding-bottom: 20px;
                                              "
                                            >
                                              <p
                                                class="b_description"
                                                style="
                                                  margin: 0;
                                                  -webkit-text-size-adjust: none;
                                                  -ms-text-size-adjust: none;
                                                  mso-line-height-rule: exactly;
                                                  font-size: 14px;
                                                  font-family: 'Open Sans',
                                                    sans-serif;
                                                  line-height: 21px;
                                                  color: #8492a6;
                                                "
                                              >
                                                We’ve taken every possible
                                                measure to keep it crisp, making
                                                sure that you enjoy the next few
                                                minutes that you’ll be spending
                                                with us. We really value your
                                                time and interest in
                                                Pattarai.<br /><br />“What
                                                problem do you want to solve
                                                today?”
                                              </p>
                                            </td>
                                          </tr>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="left"
                                              class="es-m-txt-l"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                padding-bottom: 20px;
                                              "
                                            >
                                              <span
                                                class="es-button-border"
                                                style="
                                                  border-style: solid;
                                                  background: #fbd80d;
                                                  border-width: 0px;
                                                  display: inline-block;
                                                  border-radius: 0px;
                                                  width: auto;
                                                "
                                                ><a
                                                  href="https://drive.google.com/file/d/13uZRBHHaSS5jQ9e9y1r0ECOyhLupGpqT/view?usp=sharing"
                                                  class="es-button"
                                                  target="_blank"
                                                  style="
                                                    mso-style-priority: 100 !important;
                                                    text-decoration: none;
                                                    -webkit-text-size-adjust: none;
                                                    -ms-text-size-adjust: none;
                                                    mso-line-height-rule: exactly;
                                                    font-family: 'Open Sans',
                                                      sans-serif;
                                                    font-size: 14px;
                                                    color: #000000;
                                                    border-style: solid;
                                                    border-color: #fbd80d;
                                                    border-width: 15px 30px 15px
                                                      30px;
                                                    display: inline-block;
                                                    background: #fbd80d;
                                                    border-radius: 0px;
                                                    font-weight: bold;
                                                    font-style: normal;
                                                    line-height: 17px;
                                                    width: auto;
                                                    text-align: center;
                                                  "
                                                >
                                                  <!--[if !mso]><!-- --><img
                                                    src="https://oiyomk.stripocdn.email/content/guids/CABINET_0df4df06df1e292624be9e46022c3657/images/91641606061952133.png"
                                                    alt="icon"
                                                    width="16"
                                                    style="
                                                      display: inline-block;
                                                      border: 0;
                                                      outline: none;
                                                      text-decoration: none;
                                                      -ms-interpolation-mode: bicubic;
                                                      vertical-align: middle;
                                                      margin-right: 10px;
                                                    "
                                                    align="absmiddle"
                                                  />
                                                  <!--<![endif]-->Get my
                                                  copy.</a
                                                ></span
                                              >
                                            </td>
                                          </tr>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="left"
                                              class="es-m-txt-l"
                                              style="padding: 0; margin: 0"
                                            >
                                              <span
                                                class="es-button-border"
                                                style="
                                                  border-style: solid;
                                                  border-color: #fbd80d;
                                                  background: #fbd80d;
                                                  border-width: 4px;
                                                  display: inline-block;
                                                  border-radius: 0px;
                                                  width: auto;
                                                "
                                                ><a
                                                  href="https://www.flipsnack.com/659AF9CC5A8/elevate-now_issue01.html"
                                                  class="es-button"
                                                  target="_blank"
                                                  style="
                                                    mso-style-priority: 100 !important;
                                                    text-decoration: none;
                                                    -webkit-text-size-adjust: none;
                                                    -ms-text-size-adjust: none;
                                                    mso-line-height-rule: exactly;
                                                    font-family: 'Open Sans',
                                                      sans-serif;
                                                    font-size: 14px;
                                                    color: #000000;
                                                    border-style: solid;
                                                    border-color: #fbd80d;
                                                    border-width: 10px 30px 10px
                                                      20px;
                                                    display: inline-block;
                                                    background: #fbd80d;
                                                    border-radius: 0px;
                                                    font-weight: bold;
                                                    font-style: normal;
                                                    line-height: 17px;
                                                    width: auto;
                                                    text-align: center;
                                                  "
                                                >
                                                  <!--[if !mso]><!-- --><img
                                                    src="https://oiyomk.stripocdn.email/content/guids/CABINET_0df4df06df1e292624be9e46022c3657/images/94251606062466641.png"
                                                    alt="icon"
                                                    width="20"
                                                    style="
                                                      display: inline-block;
                                                      border: 0;
                                                      outline: none;
                                                      text-decoration: none;
                                                      -ms-interpolation-mode: bicubic;
                                                      vertical-align: middle;
                                                      margin-right: 12px;
                                                    "
                                                    align="absmiddle"
                                                  />
                                                  <!--<![endif]-->Read Online</a
                                                ></span
                                              >
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <!--[if mso]></td></tr></table><![endif]-->
                            </td>
                          </tr>
                          <tr style="border-collapse: collapse">
                            <td
                              align="left"
                              style="
                                padding: 0;
                                margin: 0;
                                padding-bottom: 15px;
                                padding-left: 15px;
                                padding-right: 15px;
                              "
                            >
                              <table
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tbody>
                                  <tr style="border-collapse: collapse">
                                    <td
                                      align="center"
                                      valign="top"
                                      style="
                                        padding: 0;
                                        margin: 0;
                                        width: 570px;
                                      "
                                    >
                                      <table
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          border-collapse: collapse;
                                          border-spacing: 0px;
                                        "
                                      >
                                        <tbody>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="center"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                font-size: 0;
                                              "
                                            >
                                              <table
                                                border="0"
                                                width="100%"
                                                height="100%"
                                                cellpadding="0"
                                                cellspacing="0"
                                                role="presentation"
                                                style="
                                                  mso-table-lspace: 0pt;
                                                  mso-table-rspace: 0pt;
                                                  border-collapse: collapse;
                                                  border-spacing: 0px;
                                                "
                                              >
                                                <tbody>
                                                  <tr
                                                    style="
                                                      border-collapse: collapse;
                                                    "
                                                  >
                                                    <td
                                                      style="
                                                        padding: 0;
                                                        margin: 0;
                                                        border-bottom: 1px solid
                                                          #cccccc;
                                                        background: none;
                                                        height: 1px;
                                                        width: 100%;
                                                        margin: 0px;
                                                      "
                                                    ></td>
                                                  </tr>
                                                </tbody>
                                              </table>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </tbody>
              </table>
              <table
                class="es-footer"
                cellspacing="0"
                cellpadding="0"
                align="center"
                style="
                  mso-table-lspace: 0pt;
                  mso-table-rspace: 0pt;
                  border-collapse: collapse;
                  border-spacing: 0px;
                  table-layout: fixed !important;
                  width: 100%;
                  background-color: #141b24;
                  background-repeat: repeat;
                  background-position: center top;
                "
              >
                <tbody>
                  <tr style="border-collapse: collapse">
                    <td
                      align="center"
                      bgcolor="#000000"
                      style="padding: 0; margin: 0; background-color: #000000"
                    >
                      <table
                        class="es-footer-body"
                        cellspacing="0"
                        cellpadding="0"
                        bgcolor="#333333"
                        align="center"
                        style="
                          mso-table-lspace: 0pt;
                          mso-table-rspace: 0pt;
                          border-collapse: collapse;
                          border-spacing: 0px;
                          background-color: #333333;
                          width: 600px;
                        "
                      >
                        <tbody>
                          <tr style="border-collapse: collapse">
                            <td
                              align="left"
                              style="
                                margin: 0;
                                padding-bottom: 5px;
                                padding-left: 15px;
                                padding-right: 15px;
                                padding-top: 40px;
                              "
                            >
                              <!--[if mso]><table style="width:570px" cellpadding="0" cellspacing="0"><tr><td style="width:180px" valign="top"><![endif]-->
                              <table
                                class="es-left"
                                cellspacing="0"
                                cellpadding="0"
                                align="left"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                  float: left;
                                "
                              >
                                <tbody>
                                  <tr style="border-collapse: collapse">
                                    <td
                                      class="es-m-p20b"
                                      align="left"
                                      style="
                                        padding: 0;
                                        margin: 0;
                                        width: 180px;
                                      "
                                    >
                                      <table
                                        width="100%"
                                        cellspacing="0"
                                        cellpadding="0"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          border-collapse: collapse;
                                          border-spacing: 0px;
                                        "
                                      >
                                        <tbody>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="center"
                                              class="es-m-txt-c"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                font-size: 0px;
                                              "
                                            >
                                              <a
                                                target="_blank"
                                                href="https://www.pattarai.in/"
                                                style="
                                                  -webkit-text-size-adjust: none;
                                                  -ms-text-size-adjust: none;
                                                  mso-line-height-rule: exactly;
                                                  font-family: 'Open Sans',
                                                    sans-serif;
                                                  font-size: 12px;
                                                  text-decoration: none;
                                                  color: #ffffff;
                                                "
                                                ><img
                                                  src="https://oiyomk.stripocdn.email/content/guids/CABINET_0df4df06df1e292624be9e46022c3657/images/75971606061825273.png"
                                                  alt
                                                  style="
                                                    display: block;
                                                    border: 0;
                                                    outline: none;
                                                    text-decoration: none;
                                                    -ms-interpolation-mode: bicubic;
                                                  "
                                                  width="180"
                                              /></a>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <!--[if mso]></td><td style="width:20px"></td><td style="width:370px" valign="top"><![endif]-->
                              <table
                                class="es-right"
                                cellspacing="0"
                                cellpadding="0"
                                align="right"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                  float: right;
                                "
                              >
                                <tbody>
                                  <tr style="border-collapse: collapse">
                                    <td
                                      align="left"
                                      style="
                                        padding: 0;
                                        margin: 0;
                                        width: 370px;
                                      "
                                    >
                                      <table
                                        width="100%"
                                        cellspacing="0"
                                        cellpadding="0"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          border-collapse: collapse;
                                          border-spacing: 0px;
                                        "
                                      >
                                        <tbody>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="left"
                                              class="es-m-txt-c"
                                              style="padding: 0; margin: 0"
                                            >
                                              <h3
                                                style="
                                                  margin: 0;
                                                  line-height: 19px;
                                                  mso-line-height-rule: exactly;
                                                  font-family: roboto,
                                                    'helvetica neue', helvetica,
                                                    arial, sans-serif;
                                                  font-size: 16px;
                                                  font-style: normal;
                                                  font-weight: bold;
                                                  color: #ffffff;
                                                  letter-spacing: 0px;
                                                "
                                              >
                                                ABOUT US
                                              </h3>
                                              <p
                                                style="
                                                  margin: 0;
                                                  -webkit-text-size-adjust: none;
                                                  -ms-text-size-adjust: none;
                                                  mso-line-height-rule: exactly;
                                                  font-size: 12px;
                                                  font-family: 'Open Sans',
                                                    sans-serif;
                                                  line-height: 18px;
                                                  color: #ffffff;
                                                "
                                              >
                                                “Pattarai” is a community of
                                                industrious engineers working to
                                                transform your ideas into
                                                functioning projects! Let’s add
                                                more life to those dreams and
                                                bring them to reality to help
                                                make the world a better
                                                place!<br />
                                              </p>
                                            </td>
                                          </tr>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="left"
                                              class="es-m-txt-c"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                padding-top: 20px;
                                                font-size: 0;
                                              "
                                            >
                                              <table
                                                cellpadding="0"
                                                cellspacing="0"
                                                class="es-table-not-adapt es-social"
                                                role="presentation"
                                                style="
                                                  mso-table-lspace: 0pt;
                                                  mso-table-rspace: 0pt;
                                                  border-collapse: collapse;
                                                  border-spacing: 0px;
                                                "
                                              >
                                                <tbody>
                                                  <tr
                                                    style="
                                                      border-collapse: collapse;
                                                    "
                                                  >
                                                    <td
                                                      align="center"
                                                      valign="top"
                                                      style="
                                                        padding: 0;
                                                        margin: 0;
                                                        padding-right: 10px;
                                                      "
                                                    >
                                                      <a
                                                        target="_blank"
                                                        href="https://www.facebook.com/licetpattarai"
                                                        style="
                                                          -webkit-text-size-adjust: none;
                                                          -ms-text-size-adjust: none;
                                                          mso-line-height-rule: exactly;
                                                          font-family: 'Open Sans',
                                                            sans-serif;
                                                          font-size: 12px;
                                                          text-decoration: none;
                                                          color: #ffffff;
                                                        "
                                                        ><img
                                                          src="https://oiyomk.stripocdn.email/content/assets/img/social-icons/rounded-colored/facebook-rounded-colored.png"
                                                          alt="Fb"
                                                          title="Facebook"
                                                          width="32"
                                                          style="
                                                            display: block;
                                                            border: 0;
                                                            outline: none;
                                                            text-decoration: none;
                                                            -ms-interpolation-mode: bicubic;
                                                          "
                                                      /></a>
                                                    </td>
                                                    <td
                                                      align="center"
                                                      valign="top"
                                                      style="
                                                        padding: 0;
                                                        margin: 0;
                                                        padding-right: 10px;
                                                      "
                                                    >
                                                      <a
                                                        target="_blank"
                                                        href="https://twitter.com/licetpattarai"
                                                        style="
                                                          -webkit-text-size-adjust: none;
                                                          -ms-text-size-adjust: none;
                                                          mso-line-height-rule: exactly;
                                                          font-family: 'Open Sans',
                                                            sans-serif;
                                                          font-size: 12px;
                                                          text-decoration: none;
                                                          color: #ffffff;
                                                        "
                                                        ><img
                                                          src="https://oiyomk.stripocdn.email/content/assets/img/social-icons/rounded-colored/twitter-rounded-colored.png"
                                                          alt="Tw"
                                                          title="Twitter"
                                                          width="32"
                                                          style="
                                                            display: block;
                                                            border: 0;
                                                            outline: none;
                                                            text-decoration: none;
                                                            -ms-interpolation-mode: bicubic;
                                                          "
                                                      /></a>
                                                    </td>
                                                    <td
                                                      align="center"
                                                      valign="top"
                                                      style="
                                                        padding: 0;
                                                        margin: 0;
                                                        padding-right: 10px;
                                                      "
                                                    >
                                                      <a
                                                        target="_blank"
                                                        href="https://www.youtube.com/channel/UC24MOAmQKzWK5-6DyUaa8Aw"
                                                        style="
                                                          -webkit-text-size-adjust: none;
                                                          -ms-text-size-adjust: none;
                                                          mso-line-height-rule: exactly;
                                                          font-family: 'Open Sans',
                                                            sans-serif;
                                                          font-size: 12px;
                                                          text-decoration: none;
                                                          color: #ffffff;
                                                        "
                                                        ><img
                                                          src="https://oiyomk.stripocdn.email/content/assets/img/social-icons/rounded-colored/youtube-rounded-colored.png"
                                                          alt="Yt"
                                                          title="Youtube"
                                                          width="32"
                                                          style="
                                                            display: block;
                                                            border: 0;
                                                            outline: none;
                                                            text-decoration: none;
                                                            -ms-interpolation-mode: bicubic;
                                                          "
                                                      /></a>
                                                    </td>
                                                    <td
                                                      align="center"
                                                      valign="top"
                                                      style="
                                                        padding: 0;
                                                        margin: 0;
                                                      "
                                                    >
                                                      <a
                                                        target="_blank"
                                                        href="https://instagram.com/licetpattarai"
                                                        style="
                                                          -webkit-text-size-adjust: none;
                                                          -ms-text-size-adjust: none;
                                                          mso-line-height-rule: exactly;
                                                          font-family: 'Open Sans',
                                                            sans-serif;
                                                          font-size: 12px;
                                                          text-decoration: none;
                                                          color: #ffffff;
                                                        "
                                                        ><img
                                                          src="https://oiyomk.stripocdn.email/content/assets/img/social-icons/rounded-colored/instagram-rounded-colored.png"
                                                          alt="Ig"
                                                          title="Instagram"
                                                          width="32"
                                                          style="
                                                            display: block;
                                                            border: 0;
                                                            outline: none;
                                                            text-decoration: none;
                                                            -ms-interpolation-mode: bicubic;
                                                          "
                                                      /></a>
                                                    </td>
                                                  </tr>
                                                </tbody>
                                              </table>
                                            </td>
                                          </tr>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="left"
                                              class="es-m-txt-c"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                padding-top: 10px;
                                                font-size: 0;
                                              "
                                            >
                                              <table
                                                cellpadding="0"
                                                cellspacing="0"
                                                class="es-table-not-adapt es-social"
                                                role="presentation"
                                                style="
                                                  mso-table-lspace: 0pt;
                                                  mso-table-rspace: 0pt;
                                                  border-collapse: collapse;
                                                  border-spacing: 0px;
                                                "
                                              >
                                                <tbody>
                                                  <tr
                                                    style="
                                                      border-collapse: collapse;
                                                    "
                                                  >
                                                    <td
                                                      align="center"
                                                      valign="top"
                                                      style="
                                                        padding: 0;
                                                        margin: 0;
                                                        padding-right: 10px;
                                                      "
                                                    >
                                                      <a
                                                        target="_blank"
                                                        href="https://www.linkedin.com/company/licetpattarai"
                                                        style="
                                                          -webkit-text-size-adjust: none;
                                                          -ms-text-size-adjust: none;
                                                          mso-line-height-rule: exactly;
                                                          font-family: 'Open Sans',
                                                            sans-serif;
                                                          font-size: 12px;
                                                          text-decoration: none;
                                                          color: #ffffff;
                                                        "
                                                        ><img
                                                          src="https://oiyomk.stripocdn.email/content/guids/CABINET_0df4df06df1e292624be9e46022c3657/images/43361606061577882.png"
                                                          alt="Tw"
                                                          title="Twitter"
                                                          width="32"
                                                          style="
                                                            display: block;
                                                            border: 0;
                                                            outline: none;
                                                            text-decoration: none;
                                                            -ms-interpolation-mode: bicubic;
                                                          "
                                                      /></a>
                                                    </td>
                                                    <td
                                                      align="center"
                                                      valign="top"
                                                      style="
                                                        padding: 0;
                                                        margin: 0;
                                                      "
                                                    >
                                                      <a
                                                        target="_blank"
                                                        href="https://github.com/pattarai"
                                                        style="
                                                          -webkit-text-size-adjust: none;
                                                          -ms-text-size-adjust: none;
                                                          mso-line-height-rule: exactly;
                                                          font-family: 'Open Sans',
                                                            sans-serif;
                                                          font-size: 12px;
                                                          text-decoration: none;
                                                          color: #ffffff;
                                                        "
                                                        ><img
                                                          src="https://oiyomk.stripocdn.email/content/guids/CABINET_0df4df06df1e292624be9e46022c3657/images/78781606061610934.png"
                                                          alt="Yt"
                                                          title="Youtube"
                                                          width="32"
                                                          style="
                                                            display: block;
                                                            border: 0;
                                                            outline: none;
                                                            text-decoration: none;
                                                            -ms-interpolation-mode: bicubic;
                                                          "
                                                      /></a>
                                                    </td>
                                                  </tr>
                                                </tbody>
                                              </table>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <!--[if mso]></td></tr></table><![endif]-->
                            </td>
                          </tr>
                          <tr style="border-collapse: collapse">
                            <td
                              align="left"
                              style="
                                padding: 0;
                                margin: 0;
                                padding-left: 15px;
                                padding-right: 15px;
                                padding-top: 20px;
                              "
                            >
                              <!--[if mso]><table style="width:570px" cellpadding="0" cellspacing="0"><tr><td style="width:197px" valign="top"><![endif]-->
                              <table
                                cellpadding="0"
                                cellspacing="0"
                                class="es-left"
                                align="left"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                  float: left;
                                "
                              >
                                <tbody>
                                  <tr style="border-collapse: collapse">
                                    <td
                                      class="es-m-p0r es-m-p20b"
                                      align="center"
                                      style="
                                        padding: 0;
                                        margin: 0;
                                        width: 177px;
                                      "
                                    >
                                      <table
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          border-collapse: collapse;
                                          border-spacing: 0px;
                                        "
                                      >
                                        <tbody>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="center"
                                              style="padding: 0; margin: 0"
                                            >
                                              <span
                                                class="es-button-border"
                                                style="
                                                  border-style: solid;
                                                  background: #000000;
                                                  border-width: 0px;
                                                  display: inline-block;
                                                  border-radius: 0px;
                                                  width: auto;
                                                "
                                                ><a
                                                  href="https://www.pattarai.in/"
                                                  class="es-button"
                                                  target="_blank"
                                                  style="
                                                    mso-style-priority: 100 !important;
                                                    text-decoration: none;
                                                    -webkit-text-size-adjust: none;
                                                    -ms-text-size-adjust: none;
                                                    mso-line-height-rule: exactly;
                                                    font-family: 'Open Sans',
                                                      sans-serif;
                                                    font-size: 14px;
                                                    color: #ffffff;
                                                    border-style: solid;
                                                    border-color: #000000;
                                                    border-width: 15px 35px;
                                                    display: inline-block;
                                                    background: #000000;
                                                    border-radius: 0px;
                                                    font-weight: bold;
                                                    font-style: normal;
                                                    line-height: 17px;
                                                    width: auto;
                                                    text-align: center;
                                                  "
                                                >
                                                  <!--[if !mso]><!-- --><img
                                                    src="https://oiyomk.stripocdn.email/content/guids/CABINET_0df4df06df1e292624be9e46022c3657/images/26851606064776370.png"
                                                    alt="icon"
                                                    width="16"
                                                    style="
                                                      display: inline-block;
                                                      border: 0;
                                                      outline: none;
                                                      text-decoration: none;
                                                      -ms-interpolation-mode: bicubic;
                                                      vertical-align: middle;
                                                      margin-right: 5px;
                                                    "
                                                    align="absmiddle"
                                                  />
                                                  <!--<![endif]-->Know More</a
                                                ></span
                                              >
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                    <td
                                      class="es-hidden"
                                      style="padding: 0; margin: 0; width: 20px"
                                    ></td>
                                  </tr>
                                </tbody>
                              </table>
                              <!--[if mso]></td><td style="width:177px" valign="top"><![endif]-->
                              <table
                                cellpadding="0"
                                cellspacing="0"
                                class="es-left"
                                align="left"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                  float: left;
                                "
                              >
                                <tbody>
                                  <tr style="border-collapse: collapse">
                                    <td
                                      align="left"
                                      style="
                                        padding: 0;
                                        margin: 0;
                                        width: 177px;
                                      "
                                    >
                                      <table
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          border-collapse: collapse;
                                          border-spacing: 0px;
                                        "
                                      >
                                        <tbody>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="center"
                                              style="padding: 0; margin: 0"
                                            >
                                              <span
                                                class="es-button-border"
                                                style="
                                                  border-style: solid;
                                                  background: #000000;
                                                  border-width: 0px;
                                                  display: inline-block;
                                                  border-radius: 0px;
                                                  width: auto;
                                                "
                                                ><a
                                                  href="mailto:hello@pattarai.in?subject=Hello%20Pattarai"
                                                  class="es-button"
                                                  target="_blank"
                                                  style="
                                                    mso-style-priority: 100 !important;
                                                    text-decoration: none;
                                                    -webkit-text-size-adjust: none;
                                                    -ms-text-size-adjust: none;
                                                    mso-line-height-rule: exactly;
                                                    font-family: 'Open Sans',
                                                      sans-serif;
                                                    font-size: 14px;
                                                    color: #ffffff;
                                                    border-style: solid;
                                                    border-color: #000000;
                                                    border-width: 15px 60px;
                                                    display: inline-block;
                                                    background: #000000;
                                                    border-radius: 0px;
                                                    font-weight: bold;
                                                    font-style: normal;
                                                    line-height: 17px;
                                                    width: auto;
                                                    text-align: center;
                                                  "
                                                >
                                                  <!--[if !mso]><!-- --><img
                                                    src="https://oiyomk.stripocdn.email/content/guids/CABINET_0df4df06df1e292624be9e46022c3657/images/35631606064551163.png"
                                                    alt="icon"
                                                    width="16"
                                                    style="
                                                      display: inline-block;
                                                      border: 0;
                                                      outline: none;
                                                      text-decoration: none;
                                                      -ms-interpolation-mode: bicubic;
                                                      vertical-align: middle;
                                                      margin-right: 5px;
                                                    "
                                                    align="absmiddle"
                                                  />
                                                  <!--<![endif]-->Mail</a
                                                ></span
                                              >
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <!--[if mso]></td>
<td style="width:20px"></td><td style="width:176px" valign="top"><![endif]-->
                              <table
                                cellpadding="0"
                                cellspacing="0"
                                class="es-right"
                                align="right"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                  float: right;
                                "
                              >
                                <tbody>
                                  <tr style="border-collapse: collapse">
                                    <td
                                      align="left"
                                      style="
                                        padding: 0;
                                        margin: 0;
                                        width: 176px;
                                      "
                                    >
                                      <table
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          border-collapse: collapse;
                                          border-spacing: 0px;
                                        "
                                      >
                                        <tbody>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="center"
                                              style="padding: 0; margin: 0"
                                            >
                                              <span
                                                class="es-button-border"
                                                style="
                                                  border-style: solid;
                                                  background: #000000;
                                                  border-width: 0px;
                                                  display: inline-block;
                                                  border-radius: 0px;
                                                  width: auto;
                                                "
                                                ><a
                                                  href="tel:+919487323890"
                                                  class="es-button"
                                                  target="_blank"
                                                  style="
                                                    mso-style-priority: 100 !important;
                                                    text-decoration: none;
                                                    -webkit-text-size-adjust: none;
                                                    -ms-text-size-adjust: none;
                                                    mso-line-height-rule: exactly;
                                                    font-family: 'Open Sans',
                                                      sans-serif;
                                                    font-size: 14px;
                                                    color: #ffffff;
                                                    border-style: solid;
                                                    border-color: #000000;
                                                    border-width: 15px 60px;
                                                    display: inline-block;
                                                    background: #000000;
                                                    border-radius: 0px;
                                                    font-weight: bold;
                                                    font-style: normal;
                                                    line-height: 17px;
                                                    width: auto;
                                                    text-align: center;
                                                  "
                                                >
                                                  <!--[if !mso]><!-- --><img
                                                    src="https://oiyomk.stripocdn.email/content/guids/CABINET_0df4df06df1e292624be9e46022c3657/images/24851606064393066.png"
                                                    alt="icon"
                                                    width="16"
                                                    style="
                                                      display: inline-block;
                                                      border: 0;
                                                      outline: none;
                                                      text-decoration: none;
                                                      -ms-interpolation-mode: bicubic;
                                                      vertical-align: middle;
                                                      margin-right: 10px;
                                                    "
                                                    align="absmiddle"
                                                  />
                                                  <!--<![endif]-->Call</a
                                                ></span
                                              >
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                              <!--[if mso]></td></tr></table><![endif]-->
                            </td>
                          </tr>
                          <tr style="border-collapse: collapse">
                            <td
                              align="left"
                              style="
                                padding: 0;
                                margin: 0;
                                padding-left: 15px;
                                padding-right: 15px;
                                padding-top: 20px;
                              "
                            >
                              <table
                                cellpadding="0"
                                cellspacing="0"
                                width="100%"
                                style="
                                  mso-table-lspace: 0pt;
                                  mso-table-rspace: 0pt;
                                  border-collapse: collapse;
                                  border-spacing: 0px;
                                "
                              >
                                <tbody>
                                  <tr style="border-collapse: collapse">
                                    <td
                                      align="center"
                                      valign="top"
                                      style="
                                        padding: 0;
                                        margin: 0;
                                        width: 570px;
                                      "
                                    >
                                      <table
                                        cellpadding="0"
                                        cellspacing="0"
                                        width="100%"
                                        role="presentation"
                                        style="
                                          mso-table-lspace: 0pt;
                                          mso-table-rspace: 0pt;
                                          border-collapse: collapse;
                                          border-spacing: 0px;
                                        "
                                      >
                                        <tbody>
                                          <tr style="border-collapse: collapse">
                                            <td
                                              align="center"
                                              style="
                                                padding: 0;
                                                margin: 0;
                                                padding-bottom: 20px;
                                              "
                                            >
                                              <p
                                                style="
                                                  margin: 0;
                                                  -webkit-text-size-adjust: none;
                                                  -ms-text-size-adjust: none;
                                                  mso-line-height-rule: exactly;
                                                  font-size: 12px;
                                                  font-family: 'Open Sans',
                                                    sans-serif;
                                                  line-height: 18px;
                                                  color: #8492a6;
                                                "
                                              >
                                                © 2020&nbsp;<a
                                                  href="https://pattarai.in/"
                                                  target="_blank"
                                                  style="
                                                    -webkit-text-size-adjust: none;
                                                    -ms-text-size-adjust: none;
                                                    mso-line-height-rule: exactly;
                                                    font-family: 'Open Sans',
                                                      sans-serif;
                                                    font-size: 12px;
                                                    text-decoration: none;
                                                    color: #ffffff;
                                                  "
                                                  ><strong>Pattarai</strong></a
                                                >&nbsp;| All Rights Reserved
                                              </p>
                                            </td>
                                          </tr>
                                        </tbody>
                                      </table>
                                    </td>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </tbody>
              </table>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
</html>'''


df = pd.read_csv('list.csv')

def send_mail(name,r_mail,image):
    s_mail = "#"
    s_pass = "#"
    msg=EmailMessage()
    msg['Subject'] = f"Certificate For ReactJS WorkShop"
    msg['From'] = s_mail
    msg['To'] = r_mail
    msg.set_content(html_content,subtype="html")
    with open(image,"rb") as file:
        data = file.read()
        msg.add_attachment(data,maintype = "application", subtype = "pdf",filename = name)
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    try:
        server.login(s_mail,s_pass)
        print("Logged In Successfully")
        server.send_message(msg)
        print("Mail Sent")
        server.quit()
    except:
        print("Mail Not Sent")

for index,j in df.iterrows():
    Name = j["Name"]
    Email = j["Email"]
    Image = f"Certificate-PDF/{Name}.pdf"
    send_mail(Name , Email,Image)