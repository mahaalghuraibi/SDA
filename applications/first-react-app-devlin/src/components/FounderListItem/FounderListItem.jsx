const FounderListItem = ({name, title, founder}) => {
  return (
    <li>
      <h3>
        {name} is the best {title}!
      </h3>
      <p>{founder.credential}</p>
    </li>
  );
};

export default FounderListItem;
