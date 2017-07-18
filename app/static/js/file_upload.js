function fileUpload (
  fileField,
  signedUrlPath,
  fileUrlId,
  previewId
) {
  var file = fileField.files[0]
  if (!file) return
  getSignedURL(
    signedUrlPath,
    function (err, data, url) {
      if (err) return alert('Unable to upload file.')
      uploadFile(
        file,
        data,
        function (error) {
          if (error) return alert('Unable to upload file.')
          if (previewId != '') document.getElementById(previewId).src = url
          document.getElementById(fileUrlId).value = url
        }
      )
    }
  )

  function getSignedURL (path, cb) {
    var xhr = new XMLHttpRequest()
    xhr.open("GET", path)
    xhr.onreadystatechange = function(){
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          var response = JSON.parse(xhr.responseText)
          return cb(null, response.data, response.url)
        }
        return cb('Could not get signed URL.')
      }
    }
    xhr.send()
  }

  function uploadFile (file, s3Data, cb) {
    var xhr = new XMLHttpRequest()
    xhr.open("POST", s3Data.url)

    var postData = new FormData()
    for(key in s3Data.fields){
      postData.append(key, s3Data.fields[key])
    }
    postData.append('file', file)

    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4) {
        if (xhr.status === 200 || xhr.status === 204)
          return cb(null)

        return cb('Could not upload file.')
     }
    }
    xhr.send(postData)
  }
}
