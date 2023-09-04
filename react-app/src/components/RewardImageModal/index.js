import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { setImages } from "../../store/images";

function RewardImageFormModal(rewardId) {
  const dispatch = useDispatch();
  const { closeModal } = useModal();

  const [formData, setFormData] = useState({
    url: "",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const info = new FormData();
    info.append("url", formData.url);
    try {
      console.log("REWARD ID!!!!!!!!!", rewardId);
      const res = await fetch(`/api/rewards/${rewardId.rewardId}/image`, {
        method: "POST",
        body: info,
        credentials: "include",
      });
      console.log(res);
      if (res.ok) {
        const data = await res.json();
        console.log(data);
        closeModal();
      } else {
        const errorData = await res.json();
        console.log(errorData);
      }
    } catch (e) {
      console.log("fetch error:", e);
    }
  };

  return (
    <>
      <h1>Add an image to your project reward</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Description Image
          <input
            type="file"
            name="url"
            accept=".png, .jpeg, .jpg"
            onChange={(e) => setFormData({ ...formData, url: e.target.files[0] })}
          />
        </label>
        <button type="submit">Submit</button>
      </form>
    </>
  );
}

export default RewardImageFormModal;
