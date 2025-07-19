import axios from "axios";
import React from "react";

const TodoItem = (props) =>{
  const deleteTodoHandler = (title) => {
    axios
      .delete(`http://localhost:8000/api/todo${title}`)
      .then((res) => console.log(res));
  };

  return (
    <div>
      <p>
        <span style={{ fontWeight: "bold, underline" }}>
          {props.todo.title} :
        </span>
        {props.todo.description}
        <button
          onClick={() => deleteTodoHandler(props.todo.title)}
          className="btn btn-outline-danger my-2 mx-2"
          style={{ borderRadius: "50px" }}
        >
          x
        </button>
      </p>
      <hr></hr>
    </div>
  );
};

export default TodoItem;
