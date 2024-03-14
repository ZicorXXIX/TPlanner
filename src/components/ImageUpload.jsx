import React, { useState } from 'react';
import axios from 'axios';

function ImageUpload() {
    const [selectedFile, setSelectedFile] = React.useState();

    const fileSelectedHandler = event => {
        setSelectedFile(event.target.files[0]);
    };

    const fileUploadHandler = () => {
        const fd = new FormData();
        console.log("hello")
        fd.append('file', selectedFile);
        axios.post('http://localhost:8080/upload', fd)
            .then(res => {
                console.log(res);
            });
    };

    return (
        <div>
            <input type="file" onChange={fileSelectedHandler} />
            <button onClick={fileUploadHandler}>Upload</button>
        </div>
    );
}

export default ImageUpload;
