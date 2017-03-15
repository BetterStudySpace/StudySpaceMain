const { render } = ReactDOM

render(
		<h1 id = 'title'
			className = 'header'
			style = {{backgroundColor: 'navy', color: 'white', fontFamily: 'verdana'}}>
		Hello World
		</h1>,
	document.getElementById('react-container')
)