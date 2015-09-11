function xhr_progress() {
  console.log("xhr start");
  var xhr = $.ajaxSettings.xhr();
  //Upload progress
  xhr.upload.addEventListener("progress", function(evt) {
    if (evt.lengthComputable) {
      var percentComplete = evt.loaded / evt.total;
      //Do something with upload progress
      console.log(percentComplete);
      var progress = parseInt(percentComplete * 100)
      $('.pgs')
        .val(progress)
        .trigger('change');
    }
  }, false);

  return xhr;
}

$(document).ready(

function() {
  // form submission
  $('form').submit(function(event) {
  	event.preventDefault();
  	
    // Prevent multiple submits
    if ($.data(this, 'submitted')) return false;
    
    
    var fun_success;
    if ($(this).data('success'))
      fun_success = window[$(this).data('success')];
    else
      fun_success = function(data) {
        alert(JSON.stringify(data));
      };
	var fun_complete;
    if ($(this).data('complete'))
      fun_complete = window[$(this).data('complete')];
    else
      fun_complete = function(jqXHR, textStatus) {
      	$('.pgs-container').hide();
        console.log("submit complete. status:"+textStatus);
      };
      
    var fun_error;
    if ($(this).data('error'))
      fun_error = window[$(this).data('error')];
    else
      fun_error = function(jqXHR, textStatus, errorThrown) {
        alert("submit error. status:"+textStatus+",error:"+errorThrown);
      };	

    var formData = new FormData(this);

    console.log("submit start");
    $('.pgs-container').show();
    $.ajax({
      url: this.action,
      type: 'POST',
      data: formData,
      processData: false,
      async: true,
      xhr: xhr_progress,
      success: fun_success,
      error: fun_error,
      complete: fun_complete,
      cache: false,
      contentType: false
    });

    $.data(this, 'submitted', true); // mark form as submitted.
  });
});
