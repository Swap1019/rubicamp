document.getElementById("id_profile").addEventListener("change", function (event) {
  const preview = document.getElementById("profile-preview");
  const file = event.target.files[0];
  
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      preview.src = e.target.result;
      preview.style.display = "block";
    };
    reader.readAsDataURL(file);
  } else {
    preview.style.display = "none";
  }
});

