
"use strict";

let RC = require('./RC.js');
let Altimeter = require('./Altimeter.js');
let ThrustCommand = require('./ThrustCommand.js');
let Compass = require('./Compass.js');
let Supply = require('./Supply.js');
let HeadingCommand = require('./HeadingCommand.js');
let YawrateCommand = require('./YawrateCommand.js');
let ServoCommand = require('./ServoCommand.js');
let MotorCommand = require('./MotorCommand.js');
let VelocityZCommand = require('./VelocityZCommand.js');
let PositionXYCommand = require('./PositionXYCommand.js');
let ControllerState = require('./ControllerState.js');
let VelocityXYCommand = require('./VelocityXYCommand.js');
let RawMagnetic = require('./RawMagnetic.js');
let HeightCommand = require('./HeightCommand.js');
let AttitudeCommand = require('./AttitudeCommand.js');
let MotorStatus = require('./MotorStatus.js');
let RawRC = require('./RawRC.js');
let RuddersCommand = require('./RuddersCommand.js');
let RawImu = require('./RawImu.js');
let MotorPWM = require('./MotorPWM.js');
let PoseResult = require('./PoseResult.js');
let TakeoffAction = require('./TakeoffAction.js');
let LandingResult = require('./LandingResult.js');
let PoseFeedback = require('./PoseFeedback.js');
let TakeoffResult = require('./TakeoffResult.js');
let LandingActionGoal = require('./LandingActionGoal.js');
let TakeoffFeedback = require('./TakeoffFeedback.js');
let TakeoffActionFeedback = require('./TakeoffActionFeedback.js');
let LandingActionFeedback = require('./LandingActionFeedback.js');
let LandingFeedback = require('./LandingFeedback.js');
let TakeoffActionResult = require('./TakeoffActionResult.js');
let TakeoffGoal = require('./TakeoffGoal.js');
let LandingAction = require('./LandingAction.js');
let PoseAction = require('./PoseAction.js');
let PoseActionResult = require('./PoseActionResult.js');
let LandingActionResult = require('./LandingActionResult.js');
let PoseActionGoal = require('./PoseActionGoal.js');
let TakeoffActionGoal = require('./TakeoffActionGoal.js');
let PoseActionFeedback = require('./PoseActionFeedback.js');
let LandingGoal = require('./LandingGoal.js');
let PoseGoal = require('./PoseGoal.js');

module.exports = {
  RC: RC,
  Altimeter: Altimeter,
  ThrustCommand: ThrustCommand,
  Compass: Compass,
  Supply: Supply,
  HeadingCommand: HeadingCommand,
  YawrateCommand: YawrateCommand,
  ServoCommand: ServoCommand,
  MotorCommand: MotorCommand,
  VelocityZCommand: VelocityZCommand,
  PositionXYCommand: PositionXYCommand,
  ControllerState: ControllerState,
  VelocityXYCommand: VelocityXYCommand,
  RawMagnetic: RawMagnetic,
  HeightCommand: HeightCommand,
  AttitudeCommand: AttitudeCommand,
  MotorStatus: MotorStatus,
  RawRC: RawRC,
  RuddersCommand: RuddersCommand,
  RawImu: RawImu,
  MotorPWM: MotorPWM,
  PoseResult: PoseResult,
  TakeoffAction: TakeoffAction,
  LandingResult: LandingResult,
  PoseFeedback: PoseFeedback,
  TakeoffResult: TakeoffResult,
  LandingActionGoal: LandingActionGoal,
  TakeoffFeedback: TakeoffFeedback,
  TakeoffActionFeedback: TakeoffActionFeedback,
  LandingActionFeedback: LandingActionFeedback,
  LandingFeedback: LandingFeedback,
  TakeoffActionResult: TakeoffActionResult,
  TakeoffGoal: TakeoffGoal,
  LandingAction: LandingAction,
  PoseAction: PoseAction,
  PoseActionResult: PoseActionResult,
  LandingActionResult: LandingActionResult,
  PoseActionGoal: PoseActionGoal,
  TakeoffActionGoal: TakeoffActionGoal,
  PoseActionFeedback: PoseActionFeedback,
  LandingGoal: LandingGoal,
  PoseGoal: PoseGoal,
};
