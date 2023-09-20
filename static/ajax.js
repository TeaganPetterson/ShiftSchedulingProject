// Here I want to create a few functions that will load everytime something is changed on the page instead of waiting for a refresh
// Things like selecting a new date or shift will show the selected shifts' employees, and stuff like adding an employee to a new station will automatically save it to a database
$(document).ready(function () {
	// Attach event listeners to date and shift select elements
	$('#calendar, #selectedShift').on('change', function (event) {
		event.preventDefault()
		var selectedDate = $('#calendar').val();
		var selectedShift = $('#selectedShift').val();
		console.log(selectedDate, selectedShift)
		// Create the data object to send in the AJAX request
		var requestData = {
			calendar: selectedDate,
			selectedShift: selectedShift
		};

		// Send the AJAX request to update the selected employees for the shift
		$.ajax({
			url: '/switchShifts',
			type: 'POST',
			data: requestData,
			success: function (response) {
				// I don't think I need anything in here...
			},
			error: function (error) {
				console.error('AJAX request failed:', error);
			}
		});
	});

	// Attach event listener to the shiftAssignment form submit button
	$('#1, #2, #3, #4, #5').on('change', function (event) {
		event.preventDefault(); // Prevent the form from submitting

		// Create an object to store the selected employees for each station
		var assignmentData = {};

		// Loop through each station and get the selected employee
		// $('#shiftAssignment select').each(function () {
		var stationId = $(this).attr('id');
		var employeeShiftId = $(this).val();

		// Add the employee ID to the assignmentData object
		assignmentData[stationId] = employeeShiftId;
		// });

		// Add the selectedShift and calendar values to the assignmentData object
		assignmentData.selectedShift = $('#selectedShift').val();
		assignmentData.calendar = $('#calendar').val();

		// Send the AJAX request to create the assignments
		$.ajax({
			url: '/makeAssignments',
			type: 'POST',
			data: assignmentData,
			success: function (response) {
				// might need to add a bootstrap popup if the response is an error
				if (response.success === false) {
					//bootstrap popup

				}
			},
			error: function (error) {
				console.error('AJAX request failed:', error);
			}
		});
	});
});


function deleteAssignment(button) {
	var assId = button.getAttribute('data-employee');

	// Send an AJAX request to the server
	$.ajax({
		url: '/deleteAssignment',
		type: 'POST',
		data: { ass_id: assId },
		success: function (response) {
			if (response.success) {
				// Handle success, e.g., show a message or update the UI
				console.log('Assignment ' + assId + ' deleted successfully');

			} else {
				// Handle failure
				console.log('Failed to delete assignment');
			}
		},
		error: function (error) {
			console.error('AJAX request failed:', error);
		}
	});
	document.getElementById("submitShift").click()
}
