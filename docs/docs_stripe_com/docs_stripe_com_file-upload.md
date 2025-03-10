# File upload guide

## Use the File Upload API to securely send dispute evidence, identification documents, and more to Stripe.

When you upload a file to Stripe using the API, a file token and other
information about the file is returned. The token can then be used in other API
calls. This guide provides a detailed walk-through of this process.

## Uploading a file

To upload a file, send a `multipart/form-data` request to
**https://files.stripe.com/v1/files**. Note that the subdomain
**files.stripe.com** is different than most of Stripe’s API endpoints. The
request should specify a `purpose` and a `file`. The following example uploads a
file located at **/path/to/a/file.jpg** on your local file system with the
purpose `dispute_evidence`:

```
curl https://files.stripe.com/v1/files \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2: \
 -F "file"="@/path/to/a/file.jpg" \
 -F "purpose"="dispute_evidence"
```

The following example uploads a file using our Android SDK with the purpose
`dispute_evidence`:

```
class CheckoutActivity : AppCompatActivity() {
 private val stripe: Stripe by lazy {
 Stripe(this, "pk_test_TYooMQauvdEDq54NiTphI7jx")
 }

 private fun uploadFile(file: File) {
 stripe.createFile(
 StripeFileParams(
 file,
 StripeFilePurpose.DisputeEvidence
 ),
 callback = object : ApiResultCallback<StripeFile> {
 override fun onSuccess(result: StripeFile) {
 // File upload succeeded
 }

 override fun onError(e: Exception) {
 // File upload failed
 }

 }
 )
 }
}
```

There are [several valid
purpose](https://docs.stripe.com/api#create_file-purpose) values, each with file
format and size requirements.

PurposeDescriptionSupported mimetypesMax
sizeExpiryDownloadable`account_requirement`Additional documentation requirements
that can be requested for an account.PDFJPEGPNG16MBNEVERfalse`business_icon`A
business icon.JPEGPNGGIF512KBNEVERtrue`business_logo`A business
logo.JPEGPNGGIF512KBNEVERtrue`customer_signature`Customer signature
image.JPEGPNGSVG4MB7 daystrue`dispute_evidence`Evidence to submit with a dispute
response.PDFJPEGPNG5MB9 monthstrue`identity_document`A document to verify the
identity of an account owner during account
provisioning.PDFJPEGPNG16MBNEVERfalse`issuing_regulatory_reporting`Additional
regulatory reporting requirements for Issuing.JSON256KB2
yearstrue`pci_document`A self-assessment PCI
questionnaire.PDF16MBNEVERtrue`tax_document_user_upload`A user-uploaded tax
document.PDFCSVJPEGPNGXLSXDOCX16MBNEVERtrue`additional_verification`Additional
verification for custom
accounts.PDFJPEGPNG16MBNEVERfalse`terminal_reader_splashscreen`Splashscreen to
be displayed on Terminal readers.PNGJPEGGIF4.194304MB1 yeartrue
#### Caution

`identity_document` images also need to be smaller than 8,000px by 8,000px.

The MIME type of the file you wish to upload must correspond to its file format.

File formatMIME
typeAPKapplication/vnd.android.package-archiveCSVtext/csvDOCXapplication/vnd.openxmlformats-officedocument.wordprocessingml.documentGIFimage/gifHTMLtext/htmlJPEGimage/jpegJSONapplication/jsonJSONLapplication/jsonlMARKDOWNtext/markdownPDFapplication/pdfPEMapplication/x-pem-filePNGimage/pngSVGimage/svg+xmlTIFFimage/tiffTSVtext/tab-separated-valuesTXTtext/plainWEBPimage/webpXLSapplication/vnd.ms-excelXLSMapplication/vnd.ms-excel.sheet.macroEnabled.12XLSXapplication/vnd.openxmlformats-officedocument.spreadsheetml.sheetXMLapplication/xmlZIPapplication/zip
#### Caution

Any Microsoft Office documents containing VBA macros will be rejected due to
security concerns.

A successful request returns a [file](https://docs.stripe.com/api/files/object)
object.

## Retrieving a File API resource

To retrieve the API resource for a File, make a GET request to the **/v1/files**
endpoint of the **files.stripe.com** subdomain providing the file upload ID:

```
curl https://files.stripe.com/v1/files/{{FILE_ID}} \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2
```

When using restricted API keys, you must receive prior access to the `Files`
resource.

## Downloading File Contents

If the file purpose allows downloading the file contents, then the
[file](https://docs.stripe.com/api/files/object) includes a non-null `url` field
indicating how to access the contents. This url requires authentication with
your Stripe API keys.

```
curl https://files.stripe.com/v1/files/{{FILE_ID}}/contents
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2
```

If you want unauthenticated access to a file whose purpose allows downloading,
then you can produce anonymous download links by creating a
[file_link](https://docs.stripe.com/api#file_links).

```
curl https://api.stripe.com/v1/file_links \
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2
 -d file={{FILE_ID}}
```

The file_link resource has a `url` field that will allow unauthenticated access
to the contents of the file.

## Using a file

After a file is uploaded, the file upload ID can be used in other API requests.
For example, to attach an uploaded file to a particular dispute as evidence:

```
curl https://api.stripe.com/v1/disputes/{{DISPUTE_ID}}
 -u sk_test_BQokikJOvBiI2HlWgH4olfQ2
 -d "evidence[receipt]"={{FILE_ID}}
```

Note that you can only use an uploaded file in a single API request.

## Handling Upload Errors

When you use the File API to upload a PDF document, we run it through a series
of checks to validate that it is correctly formatted and meets PDF
specifications. We return an error for uploads that fail any of our checks.

Try the following to fix errors that we detect:

- Remove annotations or additional media you added to the document.
- If you cannot remove your annotations or media, or if you combined several
PDFs into one, try using your computer’s Print to PDF function to create a fresh
document.- [Print to PDF with
macOS](https://support.apple.com/guide/mac-help/save-a-document-as-a-pdf-on-mac-mchlp1531/mac)
- [Print to PDF with Adobe
Acrobat](https://helpx.adobe.com/acrobat/using/print-to-pdf.html)

## Links

- [several valid purpose](https://docs.stripe.com/api#create_file-purpose)
- [file](https://docs.stripe.com/api/files/object)
- [file_link](https://docs.stripe.com/api#file_links)
- [Print to PDF with
macOS](https://support.apple.com/guide/mac-help/save-a-document-as-a-pdf-on-mac-mchlp1531/mac)
- [Print to PDF with Adobe
Acrobat](https://helpx.adobe.com/acrobat/using/print-to-pdf.html)