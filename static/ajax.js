// Here I want to create a few functions that will load everytime something is changed on the page instead of waiting for a refresh
// Things like selecting a new date or shift will show the selected shifts' employees, and stuff like adding an employee to a new station will automatically save it to a database
$(document).ready(function () {
	// Attach event listeners to date and shift select elements
	$('#calendar, #selectedShift').on('change', function () {
		var selectedDate = $('#calendar').val();
		var selectedShift = $('#selectedShift').val();

		// Create the data object to send in the AJAX request
		var requestData = {
			calendar: selectedDate,
			selectedShift: selectedShift
		};

		// Send the AJAX request
		$.ajax({
			url: '/switchShifts',
			type: 'POST',
			data: requestData,
			success: function (response) {
				// Handle the response here if needed
				// You can update the UI or perform any other actions based on the response
			},
			error: function (error) {
				console.error('AJAX request failed:', error);
			}
		});
	});
});
