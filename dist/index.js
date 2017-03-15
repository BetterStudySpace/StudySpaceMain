const { render } = ReactDOM

const style = {backgroundColor: 'navy', color: 'white', fontFamily: 'century gothic'}

render(
	<div>
	<h1 id='title'
		className='header'
		style={style}>
	StudySpace	
	</h1>
	<h2 id='subtitle'
		className = 'description'
		style = {style}>
	A better way to get your shit done.
	</h2>
	</div>,
	document.getElementById('react-container')
) //render