import logo from "../imgs/logo-5.png";

const Banner = () => {
  return (
    <>
      <div className="title-container">
        <div className="title">
          <img src={logo} alt="DarkHorse Logo" className="logo-img" />
          <div>DarkHorse</div>
        </div>
      </div>
    </>
  );
};

export default Banner;
