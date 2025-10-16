// src/components/IncrementButton.jsx

const IncrementButton = (props) => {
  return (
    <button onClick={props.addOne}>Increment</button>
  );
};

export default IncrementButton;
