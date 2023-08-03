const Sequelize = require('sequelize');

const sequelize = new Sequelize('shift_planner', null, null, {
	dialect: 'postgres',
	logging: false
});

class Employee extends Sequelize.Model { }
Employee.init(
	{
		id: {
			type: Sequelize.INTEGER,
			primaryKey: true,
			autoIncrement: true
		},
		fname: {
			type: Sequelize.STRING(20),
			allowNull: false
		},
		lname: {
			type: Sequelize.STRING(20),
			allowNull: false
		}
	},
	{
		sequelize,
		modelName: 'employees',
		timestamps: false
	}
);

class EmployeeShift extends Sequelize.Model { }
EmployeeShift.init(
	{
		id: {
			type: Sequelize.INTEGER,
			primaryKey: true,
			autoIncrement: true
		},
		emp_id: {
			type: Sequelize.INTEGER,
			allowNull: false
		},
		date: {
			type: Sequelize.STRING(15),
			allowNull: false
		},
		start_time: {
			type: Sequelize.STRING(15),
			allowNull: false
		},
		end_time: {
			type: Sequelize.STRING(15),
			allowNull: false
		}
	},
	{
		sequelize,
		modelName: 'employee_shifts',
		timestamps: false
	}
);

class SetShift extends Sequelize.Model { }
SetShift.init(
	{
		id: {
			type: Sequelize.INTEGER,
			primaryKey: true,
			autoIncrement: true
		},
		start_time: {
			type: Sequelize.STRING(15),
			allowNull: false
		},
		end_time: {
			type: Sequelize.STRING(15),
			allowNull: false
		},
		display: {
			type: Sequelize.STRING(15),
			allowNull: false
		}
	},
	{
		sequelize,
		modelName: 'set_shifts',
		timestamps: false
	}
);

class Station extends Sequelize.Model { }
Station.init(
	{
		id: {
			type: Sequelize.INTEGER,
			primaryKey: true,
			autoIncrement: true
		},
		station: {
			type: Sequelize.STRING(25),
			allowNull: false
		}
	},
	{
		sequelize,
		modelName: 'stations',
		timestamps: false
	}
);

class Assignment extends Sequelize.Model { }
Assignment.init(
	{
		id: {
			type: Sequelize.INTEGER,
			primaryKey: true,
			autoIncrement: true
		},
		station_id: {
			type: Sequelize.INTEGER,
			allowNull: false
		},
		emp_id: {
			type: Sequelize.INTEGER,
			allowNull: false
		},
		shift_id: {
			type: Sequelize.INTEGER,
			allowNull: false
		},
		date: {
			type: Sequelize.STRING(15),
			allowNull: false
		}
	},
	{
		sequelize,
		modelName: 'assignments',
		timestamps: false
	}
);
