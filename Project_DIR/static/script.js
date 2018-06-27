// $(document).ready(function(){
//   $("responsive-img img").each(function(){
//     $(this).addClass("img-fluid")
//   });
// });



//for drag and drop attachment of images in markdown editor

inlineAttachment.editors.codemirror4.attach(simplemde.codemirror, {
    onFileUploadResponse: function(xhr) {
        var result = JSON.parse(xhr.responseText),
        filename = result[this.settings.jsonFieldName];

        if (result && filename) {
            var newValue;
            if (typeof this.settings.urlText === 'function') {
                newValue = this.settings.urlText.call(this, filename, result);
            } else {
                newValue = this.settings.urlText.replace(this.filenameTag, filename);
            }
            var text = this.editor.getValue().replace(this.lastValue, newValue);
            this.editor.setValue(text);
            this.settings.onFileUploaded.call(this, filename);
        }
        return false;
    }
});
