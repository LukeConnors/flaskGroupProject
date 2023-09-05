import React, { useState } from "react";
import { useModal } from "../../context/Modal";


function ImageFormModal(projectId) {
    const {closeModal} = useModal()

    const [formData, setFormData] = useState({
        url: "",
      });


    const handleSubmit = async (e) => {
        e.preventDefault();
        const info = new FormData()
        info.append("url", formData.url);
        console.log("THIS IS OUR URL", formData.url)
        try {
            const res = await fetch(`/api/projects/${projectId.projectId}/des-images`, {
              method: "POST",
              body: info,
              credentials: "include"
            });
            if (res.ok) {
              const data = await res.json();
              console.log(data);
              closeModal()
            } else {
              const errorData = await res.json();
              console.log(errorData);
            }
          } catch (e) {
            console.log("fetch error:", e);
          }
    }

return (
    <>
    <h1>Add an image to your project description</h1>
    <form onSubmit={handleSubmit}>
        <label>
            Description Image
            <input
            type="file"
            accept=".png, .jpeg, .jpg"
            onChange={(e) => setFormData({...formData, url: e.target.files[0]})}
            />
        </label>
        <button type="submit">Submit</button>
    </form>
    </>
);
}

export default ImageFormModal;
