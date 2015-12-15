I-Logix-RPY-Archive version 8.11.0 C++ 9499822
{ IProject 
	- _id = GUID d84478ea-c8fb-444f-aecc-3acdf582da60;
	- _myState = 8192;
	- _properties = { IPropertyContainer 
		- Subjects = { IRPYRawContainer 
			- size = 17;
			- value = 
			{ IPropertySubject 
				- _Name = "Activity";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "General";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "SimulationMode";
								- _Value = "TokenOriented";
								- _Type = Enum;
								- _ExtraTypeInfo = "StateOriented, TokenOriented";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "Activity_diagram";
				- Metaclasses = { IRPYRawContainer 
					- size = 10;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Action";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "ShowAction";
								- _Value = "Description";
								- _Type = Enum;
								- _ExtraTypeInfo = "Action,Description,Label";
							}
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Name";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Label,None";
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "Label";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "ActionPin";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Type";
								- _Type = Enum;
								- _ExtraTypeInfo = "";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "ActivityParameter";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Type";
								- _Type = Enum;
								- _ExtraTypeInfo = "";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "ControlFlow";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Name";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Label,None";
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
							{ IProperty 
								- _Name = "line_style";
								- _Value = "rectilinear_arrows";
								- _Type = Enum;
								- _ExtraTypeInfo = "straight_arrows,rectilinear_arrows,spline_arrows";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "DecisionNode";
						- Properties = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IProperty 
								- _Name = "CaptionBehavior";
								- _Value = "Floating";
								- _Type = Enum;
								- _ExtraTypeInfo = "Fixed,Floating";
							}
							{ IProperty 
								- _Name = "show_name";
								- _Value = "Name";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Label,None";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "DefaultTransition";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Name";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Label,None";
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
							{ IProperty 
								- _Name = "line_style";
								- _Value = "rectilinear_arrows";
								- _Type = Enum;
								- _ExtraTypeInfo = "straight_arrows,rectilinear_arrows,spline_arrows";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "ObjectFlow";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Name";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Label,None";
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
							{ IProperty 
								- _Name = "line_style";
								- _Value = "rectilinear_arrows";
								- _Type = Enum;
								- _ExtraTypeInfo = "straight_arrows,rectilinear_arrows,spline_arrows";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "StateDiagram";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Fillcolor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Swimlane";
						- Properties = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "RepresentsOnly";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Label";
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "Label";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "problem";
						- Properties = { IRPYRawContainer 
							- size = 6;
							- value = 
							{ IProperty 
								- _Name = "CommentNotation";
								- _Value = "Box_Style";
								- _Type = Enum;
								- _ExtraTypeInfo = "Note_Style,Box_Style";
							}
							{ IProperty 
								- _Name = "Compartments";
								- _Value = "Description,";
								- _Type = MultiLine;
							}
							{ IProperty 
								- _Name = "ShowAnnotationContents";
								- _Value = "Description";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Description,Label";
							}
							{ IProperty 
								- _Name = "ShowForm";
								- _Value = "Pushpin";
								- _Type = Enum;
								- _ExtraTypeInfo = "Plain,Note,Pushpin";
							}
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Relative";
								- _Type = Enum;
								- _ExtraTypeInfo = "Full_path,Relative,Name_only,Label";
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "Label";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "Animation";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "General";
						- Properties = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IProperty 
								- _Name = "AutoOpenBehavioralDiagrams";
								- _Value = "WhileStepping";
								- _Type = Enum;
								- _ExtraTypeInfo = "Never,WhileStepping,Always";
							}
							{ IProperty 
								- _Name = "EnableAutoScroll";
								- _Value = "True";
								- _Type = Bool;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "Browser";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Settings";
						- Properties = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IProperty 
								- _Name = "DisplayMode";
								- _Value = "Flat";
								- _Type = Enum;
								- _ExtraTypeInfo = "Flat,Meta-class";
							}
							{ IProperty 
								- _Name = "ShowMultipleStereotypes";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowOrder";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowStereotypes";
								- _Value = "Suffix";
								- _Type = Enum;
								- _ExtraTypeInfo = "No,Prefix,Suffix";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "CPP_CG";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Class";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "In";
								- _Value = "$type*";
								- _Type = String;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "Communication_Diagram";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "CommunicationDiagramGE";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Fillcolor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "ComponentDiagram";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "ComponentDiagramGE";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Fillcolor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "ConfigurationManagement";
				- Metaclasses = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "General";
						- Properties = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IProperty 
								- _Name = "CMTool";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "None,ClearCase,SourceIntegrity,PVCS";
							}
							{ IProperty 
								- _Name = "UseSCCtool";
								- _Value = "No";
								- _Type = Enum;
								- _ExtraTypeInfo = "Yes,No";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "SCC";
						- Properties = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IProperty 
								- _Name = "AuxProjPath";
								- _Value = "ClearCase";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "ProjName";
								- _Value = "ClearCase";
								- _Type = String;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "DeploymentDiagram";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "DeploymentDiagramGE";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Fillcolor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "Format";
				- Metaclasses = { IRPYRawContainer 
					- size = 13;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "ActionPin";
						- Properties = { IRPYRawContainer 
							- size = 5;
							- value = 
							{ IProperty 
								- _Name = "DefaultSize";
								- _Value = "0,0,12,12";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Fill.FillColor@Child.PinInArrow";
								- _Value = "$<asParent>LineColor";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Fill.FillColor@Child.PinOutArrow";
								- _Value = "$<asParent>LineColor";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "109,163,217";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineWidth";
								- _Value = "1";
								- _Type = Int;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "ActivityParameter";
						- Properties = { IRPYRawContainer 
							- size = 5;
							- value = 
							{ IProperty 
								- _Name = "DefaultSize";
								- _Value = "0,0,55,36";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Font.Font";
								- _Value = "Tahoma";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Font.Size";
								- _Value = "8";
								- _Type = Int;
							}
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "109,163,217";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineWidth";
								- _Value = "1";
								- _Type = Int;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Actor";
						- Properties = { IRPYRawContainer 
							- size = 11;
							- value = 
							{ IProperty 
								- _Name = "DefaultSize";
								- _Value = "0,0,42,84";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Fill.FillColor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Font.Font";
								- _Value = "Tahoma";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Font.Font@Child.Template";
								- _Value = "Thaoma";
								- _Type = Unknown;
							}
							{ IProperty 
								- _Name = "Font.Italic@Child.Template";
								- _Value = "0";
								- _Type = Unknown;
							}
							{ IProperty 
								- _Name = "Font.Size";
								- _Value = "8";
								- _Type = Int;
							}
							{ IProperty 
								- _Name = "Font.Size@Child.Template";
								- _Value = "8";
								- _Type = Unknown;
							}
							{ IProperty 
								- _Name = "Font.Weight@Child.NameCompartment@Name";
								- _Value = "700";
								- _Type = Int;
							}
							{ IProperty 
								- _Name = "Font.Weight@Child.Template";
								- _Value = "400";
								- _Type = Unknown;
							}
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "109,163,217";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineWidth";
								- _Value = "0";
								- _Type = Int;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Anchor";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "128,128,128";
								- _Type = Color;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Association";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "128,128,128";
								- _Type = Color;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Comment";
						- Properties = { IRPYRawContainer 
							- size = 7;
							- value = 
							{ IProperty 
								- _Name = "DefaultSize";
								- _Value = "0,0,116,60";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Fill.FillColor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Font.Font";
								- _Value = "Tahoma";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Font.Size";
								- _Value = "8";
								- _Type = Int;
							}
							{ IProperty 
								- _Name = "Font.Size@Child.NameCompartment@Stereotype";
								- _Value = "6";
								- _Type = Int;
							}
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "194,192,192";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineWidth";
								- _Value = "1";
								- _Type = Int;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "DefaultTransition";
						- Properties = { IRPYRawContainer 
							- size = 5;
							- value = 
							{ IProperty 
								- _Name = "Font.Font";
								- _Value = "Tahoma";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Font.FontColor";
								- _Value = "0,0,0";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Font.Size";
								- _Value = "8";
								- _Type = Int;
							}
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "128,128,128";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineWidth";
								- _Value = "1";
								- _Type = Int;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Depends";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "128,128,128";
								- _Type = Color;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "MergeNode";
						- Properties = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IProperty 
								- _Name = "DefaultSize";
								- _Value = "0,0,30,30";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Fill.FillColor";
								- _Value = "170,206,242";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "170,206,242";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineWidth";
								- _Value = "1";
								- _Type = Int;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Note";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Fill.FillColor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Package";
						- Properties = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IProperty 
								- _Name = "Fill.FillColor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "109,163,217";
								- _Type = Color;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "UseCase";
						- Properties = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IProperty 
								- _Name = "Fill.FillColor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "109,163,217";
								- _Type = Color;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "problem";
						- Properties = { IRPYRawContainer 
							- size = 7;
							- value = 
							{ IProperty 
								- _Name = "DefaultSize";
								- _Value = "0,0,116,60";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Fill.FillColor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Font.Font";
								- _Value = "Tahoma";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "Font.Size";
								- _Value = "8";
								- _Type = Int;
							}
							{ IProperty 
								- _Name = "Font.Size@Child.NameCompartment@Stereotype";
								- _Value = "6";
								- _Type = Int;
							}
							{ IProperty 
								- _Name = "Line.LineColor";
								- _Value = "194,192,192";
								- _Type = Color;
							}
							{ IProperty 
								- _Name = "Line.LineWidth";
								- _Value = "1";
								- _Type = Int;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "General";
				- Metaclasses = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Graphics";
						- Properties = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IProperty 
								- _Name = "ActivityDiagramToolbar";
								- _Value = "RpyDefault,ActivityFinal,DecisionNode";
								- _Type = String;
							}
							{ IProperty 
								- _Name = "ExportedDiagramScale";
								- _Value = "NoPagination";
								- _Type = Enum;
								- _ExtraTypeInfo = "FitToOnePage,NoPagination,UsePrintLayout";
							}
							{ IProperty 
								- _Name = "Tool_tips";
								- _Value = "False";
								- _Type = Bool;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Model";
						- Properties = { IRPYRawContainer 
							- size = 9;
							- value = 
							{ IProperty 
								- _Name = "AutoSaveInterval";
								- _Value = "30";
								- _Type = Int;
							}
							{ IProperty 
								- _Name = "DescriptionEditor";
								- _Value = "C:\\Program Files\\Microsoft Office 15\\root\\office15\\WINWORD.EXE";
								- _Type = File;
							}
							{ IProperty 
								- _Name = "OutputWindowFont";
								- _Value = "Courier New 9 NoBold NoItalic";
								- _Type = Font;
							}
							{ IProperty 
								- _Name = "ShowModelTooltipInBrowser";
								- _Value = "Simple";
								- _Type = Enum;
								- _ExtraTypeInfo = "Enhanced,Simple";
							}
							{ IProperty 
								- _Name = "ShowModelTooltipInDescription";
								- _Value = "Simple";
								- _Type = Enum;
								- _ExtraTypeInfo = "Enhanced,Simple";
							}
							{ IProperty 
								- _Name = "ShowModelTooltipInGrid";
								- _Value = "Simple";
								- _Type = Enum;
								- _ExtraTypeInfo = "Enhanced,Simple";
							}
							{ IProperty 
								- _Name = "ShowModelTooltipInMenu";
								- _Value = "Simple";
								- _Type = Enum;
								- _ExtraTypeInfo = "Enhanced,Simple";
							}
							{ IProperty 
								- _Name = "ShowModelTooltipInSearchResult";
								- _Value = "Simple";
								- _Type = Enum;
								- _ExtraTypeInfo = "Enhanced,Simple";
							}
							{ IProperty 
								- _Name = "SourceFont";
								- _Value = "Courier New 9 NoBold NoItalic";
								- _Type = Font;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "ObjectModelGe";
				- Metaclasses = { IRPYRawContainer 
					- size = 4;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Actor";
						- Properties = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Name_only";
								- _Type = Enum;
								- _ExtraTypeInfo = "Full_path,Relative,Name_only,Label";
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Block";
						- Properties = { IRPYRawContainer 
							- size = 9;
							- value = 
							{ IProperty 
								- _Name = "Compartments";
								- _Value = "";
								- _Type = MultiLine;
							}
							{ IProperty 
								- _Name = "ShowAttributes";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "All,None,Public,Explicit";
							}
							{ IProperty 
								- _Name = "ShowInheritedAttributes";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowInheritedOperations";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Name_only";
								- _Type = Enum;
								- _ExtraTypeInfo = "Full_path,Relative,Name_only,Label";
							}
							{ IProperty 
								- _Name = "ShowOperations";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "All,None,Public,Explicit";
							}
							{ IProperty 
								- _Name = "ShowPorts";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowPortsInterfaces";
								- _Value = "False";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "Label";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "ClassDiagram";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Fillcolor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "Comment";
						- Properties = { IRPYRawContainer 
							- size = 6;
							- value = 
							{ IProperty 
								- _Name = "CommentNotation";
								- _Value = "Box_Style";
								- _Type = Enum;
								- _ExtraTypeInfo = "Note_Style,Box_Style";
							}
							{ IProperty 
								- _Name = "Compartments";
								- _Value = "Description,";
								- _Type = MultiLine;
							}
							{ IProperty 
								- _Name = "ShowAnnotationContents";
								- _Value = "Description";
								- _Type = Enum;
								- _ExtraTypeInfo = "Name,Description,Label";
							}
							{ IProperty 
								- _Name = "ShowForm";
								- _Value = "Pushpin";
								- _Type = Enum;
								- _ExtraTypeInfo = "Plain,Note,Pushpin";
							}
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Relative";
								- _Type = Enum;
								- _ExtraTypeInfo = "Full_path,Relative,Name_only,Label";
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "Label";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "PanelDiagram";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "General";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Fillcolor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "SequenceDiagram";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "SequenceDiagram";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Fillcolor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "StatechartDiagram";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "StateDiagram";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Fillcolor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "TestConductor";
				- Metaclasses = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "Settings";
						- Properties = { IRPYRawContainer 
							- size = 6;
							- value = 
							{ IProperty 
								- _Name = "AcknowledgeApplyChanges";
								- _Value = "True";
								- _Type = Bool;
							}
							{ IProperty 
								- _Name = "CreateTestArchitectureMode";
								- _Value = "Standard";
								- _Type = Enum;
								- _ExtraTypeInfo = "Standard,Advanced";
							}
							{ IProperty 
								- _Name = "MapSDToTestArchitectureMode";
								- _Value = "Strict";
								- _Type = Enum;
								- _ExtraTypeInfo = "Strict,Weak";
							}
							{ IProperty 
								- _Name = "OverwriteTestContextDiagram";
								- _Value = "Never";
								- _Type = Enum;
								- _ExtraTypeInfo = "Never,Always,AskUser";
							}
							{ IProperty 
								- _Name = "TestCaseExecutionOrder";
								- _Value = "BrowserOrder";
								- _Type = Enum;
								- _ExtraTypeInfo = "BrowserOrder,DeclarationOrder";
							}
							{ IProperty 
								- _Name = "TestingMode";
								- _Value = "AssertionBased";
								- _Type = Enum;
								- _ExtraTypeInfo = "AnimationBased,AssertionBased";
							}
						}
					}
				}
			}
			{ IPropertySubject 
				- _Name = "UseCaseGe";
				- Metaclasses = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertyMetaclass 
						- _Name = "UseCase";
						- Properties = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IProperty 
								- _Name = "ShowName";
								- _Value = "Name_only";
								- _Type = Enum;
								- _ExtraTypeInfo = "Full_path,Relative,Name_only,Label";
							}
							{ IProperty 
								- _Name = "ShowStereotype";
								- _Value = "None";
								- _Type = Enum;
								- _ExtraTypeInfo = "Label,Bitmap,None";
							}
						}
					}
					{ IPropertyMetaclass 
						- _Name = "UseCaseDiagram";
						- Properties = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IProperty 
								- _Name = "Fillcolor";
								- _Value = "255,255,255";
								- _Type = Color;
							}
						}
					}
				}
			}
		}
	}
	- _name = "SysEngDevEnv";
	- Stereotypes = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IHandle 
			- _m2Class = "IStereotype";
			- _filename = "$OMROOT\\Profiles\\SysML\\SysMLProfile_rpy\\SysML.sbs";
			- _subsystem = "SysML";
			- _class = "";
			- _name = "SysML";
			- _id = GUID 052b8171-a32b-4f45-a829-5585f79f9deb;
		}
	}
	- _modifiedTimeWeak = 12.14.2015::15:21:10;
	- _lastID = 33;
	- _unitSccProjName = "ClearCase";
	- _unitSccProjPath = "ClearCase";
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "Model_Walkthrough.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "Model Walkthrough";
		- _id = GUID c257fb7c-0e1f-4030-919b-d384e2804c01;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "DefaultComponent.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "DefaultComponent";
		- _id = GUID bfdb8f53-2bc6-49d2-8bed-99a758995a97;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 9;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 84;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = 4;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = 7;
		}
		{ IMultiplicityItem 
			- _name = "1..5";
			- _count = 0;
		}
		{ IMultiplicityItem 
			- _name = "4";
			- _count = 1;
		}
		{ IMultiplicityItem 
			- _name = "0..4";
			- _count = 0;
		}
		{ IMultiplicityItem 
			- _name = "2";
			- _count = 2;
		}
		{ IMultiplicityItem 
			- _name = "1..3";
			- _count = 2;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 22;
		- value = 
		{ IProfile 
			- fileName = "SysML";
			- _persistAs = "$OMROOT\\Profiles\\SysML\\SysMLProfile_rpy";
			- _id = GUID d9689b73-885e-44c4-896b-de43defa0a33;
			- _isReference = 1;
		}
		{ IProfile 
			- fileName = "SE_Dev_Profile";
			- _id = GUID b505e3dc-e3bc-489b-b15d-d48ef5689d67;
		}
		{ IProfile 
			- fileName = "DocGen_Profile";
			- _persistAs = "$SCRIPTROOT\\DocGen";
			- _id = GUID 2ded90a0-df63-48d4-997c-2dded836f245;
			- _name = "DocGen Profile";
			- _isReference = 1;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre80Cpp";
			- _id = GUID cdc61ea8-5d48-43f9-9f97-af672c36c918;
		}
		{ IProfile 
			- fileName = "SysML_Pre80.sbs";
			- _id = GUID 4b435a8c-5c01-4ecd-a419-aa0b116ac54d;
			- _name = "SysML_Pre80";
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre803Cpp";
			- _id = GUID 2c6673a1-7843-43a4-92d5-93795ef7e229;
		}
		{ IProfile 
			- fileName = "SysML_Pre803.sbs";
			- _id = GUID 67eda4ca-5ff1-42c5-a7ef-804c356b1cec;
			- _name = "SysML_Pre803";
		}
		{ ISubsystem 
			- fileName = "Model_Walkthrough";
			- _id = GUID c257fb7c-0e1f-4030-919b-d384e2804c01;
			- _name = "Model Walkthrough";
		}
		{ ISubsystem 
			- fileName = "Product_Development_Domain_Structure";
			- _id = GUID b2fd3195-49dd-4b59-ad74-413fa43b0f78;
			- _name = "Product Development Domain Structure";
		}
		{ ISubsystem 
			- _id = GUID 6bca94b1-3700-4982-9b60-2821c4b41793;
			- _myState = 8192;
			- _name = "SE Life Cycle Workflow Use Cases";
			- _modifiedTimeWeak = 12.14.2015::15:21:10;
			- _theMainDiagram = { IHandle 
				- _m2Class = "IDiagram";
				- _id = GUID 5eb2f333-93d6-437c-aabe-47136547f99d;
			}
			- _lastID = 21;
			- Declaratives = { IRPYRawContainer 
				- size = 8;
				- value = 
				{ ISubsystem 
					- _id = GUID c469f8a5-924d-4311-8ccb-368e28548a19;
					- _myState = 8192;
					- _name = "Use Case Table Views";
					- _modifiedTimeWeak = 12.14.2015::15:21:10;
					- _theMainDiagram = { IHandle 
						- _m2Class = "IDiagram";
						- _id = GUID 5eb2f333-93d6-437c-aabe-47136547f99d;
					}
					- _lastID = 7;
					- Declaratives = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ ISubsystem 
							- _id = GUID d055f618-defb-432d-bb0e-0ca8d7a21e23;
							- _myState = 8192;
							- _name = "Layouts";
							- _modifiedTimeWeak = 9.22.2015::19:35:26;
							- _lastID = 5;
							- weakCGTime = 9.22.2015::19:35:26;
							- strongCGTime = 3.29.2015::15:52:25;
							- _defaultComposite = GUID bbbd3333-2dfa-4340-9395-df75e84cca70;
							- _eventsBaseID = -1;
							- Classes = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IClass 
									- _id = GUID bbbd3333-2dfa-4340-9395-df75e84cca70;
									- _myState = 40960;
									- _name = "TopLevel";
									- _modifiedTimeWeak = 3.29.2015::15:52:25;
									- weakCGTime = 3.29.2015::15:52:25;
									- strongCGTime = 3.29.2015::15:52:25;
									- _multiplicity = "";
									- _itsStateChart = { IHandle 
										- _m2Class = "";
									}
									- _classModifier = Unspecified;
								}
							}
							- TableLayouts = { IRPYRawContainer 
								- size = 18;
								- value = 
								{ ITableLayout 
									- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 2;
															- value = 
															{ IProperty 
																- _Name = "CollapseFirstColumn";
																- _Value = "True";
																- _Type = Bool;
															}
															{ IProperty 
																- _Name = "EnableCriteriaCheck";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "Use Cases Actor Layout";
									- _modifiedTimeWeak = 11.17.2014::14:8:51;
									- Tags = { IRPYRawContainer 
										- size = 2;
										- value = 
										{ ITag 
											- _id = GUID c0925fa8-2548-401d-9781-e5db23ed78a7;
											- _myState = 8192;
											- _name = "Conform_Viewpoint";
											- _modifiedTimeWeak = 2.27.2014::16:28:31;
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID 0a6de72f-1bd8-41dc-bc41-86f7c2a0296a;
											- _myState = 8192;
											- _name = "Or_And_Veiwpoint";
											- _modifiedTimeWeak = 2.27.2014::16:31:17;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 1ad39237-1077-4591-8a62-ecf7a130d627;
													- _modifiedTimeWeak = 2.27.2014::16:31:17;
													- _value = "or";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "AssociationEnd";
											- _DataType = 2;
										}
									}
									- DataColumns = { IRPYRawContainer 
										- size = 3;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "RelationTo.To element";
											- _columnName = "Use Case";
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "RelationFrom.From element";
											- _columnName = "Actors";
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Stereotypes";
											- _columnName = "Primary Actor Identifier";
										}
									}
									- m_RelationTable = 1;
									- m_CollapseFirstColumn = 1;
									- TableFromElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "Actor";
											- _DataType = 2;
										}
									}
									- TableToElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
								}
								{ ITableLayout 
									- _id = GUID 1b7fef36-dd14-49fa-909c-2a358af3a2a2;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 2;
															- value = 
															{ IProperty 
																- _Name = "CollapseFirstColumn";
																- _Value = "False";
																- _Type = Bool;
															}
															{ IProperty 
																- _Name = "EnableCriteriaCheck";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "Use Cases Description and Stage Layout";
									- _modifiedTimeWeak = 7.24.2015::14:44:6;
									- Tags = { IRPYRawContainer 
										- size = 2;
										- value = 
										{ ITag 
											- _id = GUID 494419c0-698e-4cd2-a86f-9f13d4e5e36c;
											- _myState = 8192;
											- _name = "Conform_Viewpoint";
											- _modifiedTimeWeak = 2.5.2014::14:42:54;
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID 5b5f905b-e6d8-4486-a02d-9996f1edb9f5;
											- _myState = 8192;
											- _name = "Or_And_Veiwpoint";
											- _modifiedTimeWeak = 2.5.2014::14:43:10;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID f99e3f7a-0fe7-48eb-938e-0022ca50ba82;
													- _modifiedTimeWeak = 2.5.2014::14:43:10;
													- _value = "or";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 1b7fef36-dd14-49fa-909c-2a358af3a2a2;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
									- DataColumns = { IRPYRawContainer 
										- size = 3;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 1b7fef36-dd14-49fa-909c-2a358af3a2a2;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Name";
											- _columnName = "Use Case";
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 1b7fef36-dd14-49fa-909c-2a358af3a2a2;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Owner";
											- _columnName = "Stage";
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 1b7fef36-dd14-49fa-909c-2a358af3a2a2;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Description";
											- _columnName = "Description";
										}
									}
									- TableFromElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "Actor";
											- _DataType = 2;
										}
									}
									- TableToElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
								}
								{ ITableLayout 
									- _id = GUID 9b19ab13-1b37-4fb0-a743-a39d49044c20;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 1;
															- value = 
															{ IProperty 
																- _Name = "CollapseFirstColumn";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "UCImporter";
									- Stereotypes = { IRPYRawContainer 
										- size = 2;
										- value = 
										{ IHandle 
											- _m2Class = "IStereotype";
											- _filename = "PredefinedTypes.sbs";
											- _subsystem = "PredefinedTypes";
											- _class = "";
											- _name = "CSVImporter";
											- _id = GUID 00a7dd46-a903-43ea-8ba3-6e9b23f98be1;
										}
										{ IHandle 
											- _m2Class = "IStereotype";
											- _filename = "PredefinedTypes.sbs";
											- _subsystem = "PredefinedTypes";
											- _class = "";
											- _name = "CSVImporter";
											- _id = GUID 00a7dd46-a903-43ea-8ba3-6e9b23f98be1;
										}
									}
									- _modifiedTimeWeak = 3.12.2014::14:29:4;
									- Tags = { IRPYRawContainer 
										- size = 3;
										- value = 
										{ ITag 
											- _id = GUID d45bcd49-8b31-45d6-9655-2090a6af11c6;
											- _myState = 8192;
											- _name = "Ignore_First_Row";
											- Stereotypes = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IHandle 
													- _m2Class = "IStereotype";
													- _filename = "PredefinedTypes.sbs";
													- _subsystem = "PredefinedTypes";
													- _class = "";
													- _name = "HideInBrowser";
													- _id = GUID ce41754a-c9a3-49a9-a336-73ac03345c2f;
												}
											}
											- _modifiedTimeWeak = 2.27.2014::17:34:26;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID d1895b37-c3ed-4476-8889-4289dcbbf377;
													- _modifiedTimeWeak = 2.27.2014::17:34:26;
													- _value = "True";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpBoolean";
												- _id = GUID f19b56f2-78ab-44fa-860e-6ead487ecb07;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "CSVImporter";
												- _name = "Ignore_First_Row";
												- _id = GUID 35db43e5-ebc1-4522-834a-c95f69aa781c;
											}
										}
										{ ITag 
											- _id = GUID 72a02fee-8d82-475b-b4b3-f900683cd677;
											- _myState = 8192;
											- _name = "Source_Import_Files";
											- Stereotypes = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IHandle 
													- _m2Class = "IStereotype";
													- _filename = "PredefinedTypes.sbs";
													- _subsystem = "PredefinedTypes";
													- _class = "";
													- _name = "HideInBrowser";
													- _id = GUID ce41754a-c9a3-49a9-a336-73ac03345c2f;
												}
											}
											- _modifiedTimeWeak = 2.27.2014::17:34:26;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 07642b16-b321-4f71-9d8d-6cb9289cc170;
													- _modifiedTimeWeak = 2.27.2014::17:34:26;
													- _value = "C:\\Users\\watsonjc\\Desktop\\Temp UCs.csv";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "CSVImporter";
												- _name = "Source_Import_Files";
												- _id = GUID 08d20c06-dc12-42f5-8319-999b8f4d7925;
											}
										}
										{ ITag 
											- _id = GUID 9c176d8b-51f6-43ab-905a-e7c2c9d780b1;
											- _myState = 8192;
											- _name = "Target_Model_Element";
											- Stereotypes = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IHandle 
													- _m2Class = "IStereotype";
													- _filename = "PredefinedTypes.sbs";
													- _subsystem = "PredefinedTypes";
													- _class = "";
													- _name = "HideInBrowser";
													- _id = GUID ce41754a-c9a3-49a9-a336-73ac03345c2f;
												}
											}
											- _modifiedTimeWeak = 2.27.2014::21:34:30;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IInstanceValue 
													- _id = GUID 9b553fce-7b06-427b-9779-ee038d7bb36b;
													- _modifiedTimeWeak = 1.2.1990::0:0:0;
													- _value = { IHandle 
														- _m2Class = "ISubsystem";
														- _filename = "SE_Domain_Workflow_Use_Cases.sbs";
														- _subsystem = "SE Life Cycle Workflow Use Cases::System Development Stage";
														- _class = "";
														- _name = "SE Domain Workflow Use Cases";
														- _id = GUID 81c5a56b-9b7c-4c90-97ad-f11f8d46ddf9;
													}
												}
											}
											- myTypeOf = { IType 
												- _id = GUID 01b8249b-73a2-4779-ac3b-bb311011081b;
												- _myState = 8192;
												- _modifiedTimeWeak = 1.2.1990::0:0:0;
												- _declaration = "Package";
												- _kind = Language;
											}
											- _isOrdered = 0;
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 9b19ab13-1b37-4fb0-a743-a39d49044c20;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
									- DataColumns = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 9b19ab13-1b37-4fb0-a743-a39d49044c20;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Name";
										}
									}
								}
								{ ITableLayout 
									- _id = GUID 0de9637a-ba26-43f4-9159-5beb301e6c29;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 1;
															- value = 
															{ IProperty 
																- _Name = "CollapseFirstColumn";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "Use Case List and Organization";
									- _modifiedTimeWeak = 5.18.2015::19:40:38;
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0de9637a-ba26-43f4-9159-5beb301e6c29;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
									- DataColumns = { IRPYRawContainer 
										- size = 4;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0de9637a-ba26-43f4-9159-5beb301e6c29;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Owner";
											- _columnName = "Category";
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0de9637a-ba26-43f4-9159-5beb301e6c29;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Name";
											- _columnName = "Use Case";
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0de9637a-ba26-43f4-9159-5beb301e6c29;
											}
											- _modelElement = { IHandle 
												- _m2Class = "ITag";
												- _filename = "SE_Dev_Profile.sbs";
												- _subsystem = "SE_Dev_Profile";
												- _class = "UC_Properties";
												- _name = "Priority";
												- _id = GUID 8f6c2f6d-1d8d-40d2-9569-d028cb8174cd;
											}
											- _name = "Priority";
											- _DataType = 6;
											- _columnName = "Priority";
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0de9637a-ba26-43f4-9159-5beb301e6c29;
											}
											- _modelElement = { IHandle 
												- _m2Class = "ITag";
												- _filename = "SE_Dev_Profile.sbs";
												- _subsystem = "SE_Dev_Profile";
												- _class = "UC_Properties";
												- _name = "Maturity";
												- _id = GUID f585f3bb-6906-4f3c-83e9-397f5798fed9;
											}
											- _name = "Maturity";
											- _DataType = 6;
											- _columnName = "Maturity Level";
										}
									}
								}
								{ ITableLayout 
									- _id = GUID 8d318d1b-111e-4a8e-9a9c-4f30e723aca8;
									- _myState = 8192;
									- _name = "Use Case Status Layout";
									- Stereotypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IHandle 
											- _m2Class = "IStereotype";
											- _filename = "PredefinedTypes.sbs";
											- _subsystem = "PredefinedTypes";
											- _class = "";
											- _name = "MetricsLayout";
											- _id = GUID d7835c5f-d908-47bc-8bab-f37bc3dd3f8a;
										}
									}
									- _modifiedTimeWeak = 9.22.2015::19:35:26;
									- Tags = { IRPYRawContainer 
										- size = 2;
										- value = 
										{ ITag 
											- _id = GUID 236fe128-2922-49aa-938f-f5bb4cd392b2;
											- _myState = 8192;
											- _name = "Metrics_Queries";
											- _modifiedTimeWeak = 9.22.2015::19:35:26;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 8;
												- value = 
												{ IInstanceValue 
													- _id = GUID 5ec9fe05-d7da-4c88-945a-2ba27936078a;
													- _modifiedTimeWeak = 1.2.1990::0:0:0;
													- _value = { IHandle 
														- _m2Class = "ITableLayout";
														- _id = GUID b37edbeb-f2e8-4e59-8b34-e0f82efce15e;
													}
												}
												{ IInstanceValue 
													- _id = GUID 766f8d98-1904-4e85-97bc-f89ee50287a4;
													- _modifiedTimeWeak = 1.2.1990::0:0:0;
													- _value = { IHandle 
														- _m2Class = "ITableLayout";
														- _id = GUID ffbfc210-bda3-4fe5-a692-55af76f2d7a2;
													}
												}
												{ IInstanceValue 
													- _id = GUID 7738ee9f-4835-45d6-80b3-ab38f82b6287;
													- _modifiedTimeWeak = 1.2.1990::0:0:0;
													- _value = { IHandle 
														- _m2Class = "ITableLayout";
														- _id = GUID fab21e02-ecda-4e2c-b597-4a0cfeb1a3e2;
													}
												}
												{ IInstanceValue 
													- _id = GUID 3631590a-8778-45d5-84b4-b2059fb2106a;
													- _modifiedTimeWeak = 1.2.1990::0:0:0;
													- _value = { IHandle 
														- _m2Class = "ITableLayout";
														- _id = GUID 399e5f15-af07-4539-b24a-c5d3e13a1ecb;
													}
												}
												{ IInstanceValue 
													- _id = GUID 713e1d91-7d3a-41d0-b833-50fb4f189f38;
													- _modifiedTimeWeak = 1.2.1990::0:0:0;
													- _value = { IHandle 
														- _m2Class = "ITableLayout";
														- _id = GUID fb0bfc59-6c0f-4401-bb9c-f7108e9d0b71;
													}
												}
												{ IInstanceValue 
													- _id = GUID 8702a129-2fa7-4c6d-b09d-0c210fbad54c;
													- _modifiedTimeWeak = 1.2.1990::0:0:0;
													- _value = { IHandle 
														- _m2Class = "ITableLayout";
														- _id = GUID a7b7c326-6f55-48b0-90f3-124b45d35301;
													}
												}
												{ IInstanceValue 
													- _id = GUID bc5661dc-49f2-430f-a267-a713e5768c0c;
													- _modifiedTimeWeak = 1.2.1990::0:0:0;
													- _value = { IHandle 
														- _m2Class = "ITableLayout";
														- _id = GUID f05ebfd0-60a4-45e1-9af7-52c148a77bda;
													}
												}
												{ IInstanceValue 
													- _id = GUID 0da6d238-dbe4-4d25-97b8-49cc3ef53308;
													- _modifiedTimeWeak = 1.2.1990::0:0:0;
													- _value = { IHandle 
														- _m2Class = "ITableLayout";
														- _id = GUID 56077a4f-2001-49fd-89f6-9216891aaaf3;
													}
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IStereotype";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "Query";
												- _id = GUID 4c77a3b1-822f-466e-bd06-76145c9e3b88;
											}
											- _multiplicity = "*";
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "MetricsLayout";
												- _name = "Metrics_Queries";
												- _id = GUID f6d06c05-ea54-4369-9911-525acc2a6513;
											}
										}
										{ ITag 
											- _id = GUID ddb08c59-2e40-43cf-bca2-9e14b8479ec5;
											- _myState = 8192;
											- _name = "Metrics_DisplayTextList";
											- _modifiedTimeWeak = 9.22.2015::19:35:26;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 8;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID bdf27acd-ed67-4c6b-9559-ba02db653f22;
													- _modifiedTimeWeak = 9.22.2015::19:35:26;
													- _value = "Total Use Case";
												}
												{ ILiteralSpecification 
													- _id = GUID 01c5a8e9-05e3-440c-ae27-f19af0db6984;
													- _modifiedTimeWeak = 9.22.2015::19:35:26;
													- _value = "UC - Goal Only";
												}
												{ ILiteralSpecification 
													- _id = GUID b6fe6078-c9af-4940-a80e-c2d895401e16;
													- _modifiedTimeWeak = 9.22.2015::19:35:26;
													- _value = "UC -Early Text Description";
												}
												{ ILiteralSpecification 
													- _id = GUID 0b0ba87f-b7e1-4b56-a803-f4e6c1b89ee7;
													- _modifiedTimeWeak = 9.22.2015::19:35:26;
													- _value = "UC - Evolving Description";
												}
												{ ILiteralSpecification 
													- _id = GUID cfa585c1-3276-4c77-a05c-a275e39af5d0;
													- _modifiedTimeWeak = 9.22.2015::19:35:26;
													- _value = "UC - Description Reviewed";
												}
												{ ILiteralSpecification 
													- _id = GUID b912436d-b340-4ca4-8291-3f2b534e6ff2;
													- _modifiedTimeWeak = 9.22.2015::19:35:26;
													- _value = "UC - Early Activity";
												}
												{ ILiteralSpecification 
													- _id = GUID 6eb8f6db-ac40-43ae-b7df-4d833a257643;
													- _modifiedTimeWeak = 9.22.2015::19:35:26;
													- _value = "UC - Evolving Activity";
												}
												{ ILiteralSpecification 
													- _id = GUID 97228526-28da-4171-907d-c0b1085fd057;
													- _modifiedTimeWeak = 9.22.2015::19:35:26;
													- _value = "UC - Activity Complete";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _multiplicity = "*";
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "MetricsLayout";
												- _name = "Metrics_DisplayTextList";
												- _id = GUID b1882670-b0d0-444e-b105-31acffa34282;
											}
										}
									}
								}
								{ ITableLayout 
									- _id = GUID ffbfc210-bda3-4fe5-a692-55af76f2d7a2;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 1;
															- value = 
															{ IProperty 
																- _Name = "EnableCriteriaCheck";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "UC - Goal Only";
									- Stereotypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IHandle 
											- _m2Class = "IStereotype";
											- _filename = "PredefinedTypes.sbs";
											- _subsystem = "PredefinedTypes";
											- _class = "";
											- _name = "Query";
											- _id = GUID 4c77a3b1-822f-466e-bd06-76145c9e3b88;
										}
									}
									- _modifiedTimeWeak = 6.9.2014::17:11:4;
									- Tags = { IRPYRawContainer 
										- size = 4;
										- value = 
										{ ITag 
											- _id = GUID 3e793b96-5665-4f1d-9e6a-001dc4c4e1c5;
											- _myState = 8192;
											- _name = "Tag_Name";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 677a2868-d125-4e19-8ee2-80cf1aedd722;
													- _modifiedTimeWeak = 6.9.2014::17:8:12;
													- _value = "Maturity";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Name";
												- _id = GUID 3358798e-bfb4-426b-a12d-552274ee65e5;
											}
										}
										{ ITag 
											- _id = GUID b102b884-886f-4aaf-9537-42c5d35be0c1;
											- _myState = 8192;
											- _name = "Tag_Value";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 7ab201d8-1d87-4f68-b399-f4c31ee97467;
													- _modifiedTimeWeak = 6.9.2014::17:8:12;
													- _value = "Goal Only";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Value";
												- _id = GUID 41c58abd-ed56-47c6-80e0-88ce9852cd43;
											}
										}
										{ ITag 
											- _id = GUID 9ab14090-0612-4226-b61d-bbfee984dbdd;
											- _myState = 8192;
											- _name = "Conform_Viewpoint";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID ef05c6ce-00aa-4511-bac0-c39bd89c1cab;
											- _myState = 8192;
											- _name = "Or_And_Veiwpoint";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 12a982ad-506a-4db0-bca2-f1c00dff7e1b;
													- _modifiedTimeWeak = 6.9.2014::17:8:12;
													- _value = "or";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 399e5f15-af07-4539-b24a-c5d3e13a1ecb;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
								}
								{ ITableLayout 
									- _id = GUID fab21e02-ecda-4e2c-b597-4a0cfeb1a3e2;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 1;
															- value = 
															{ IProperty 
																- _Name = "EnableCriteriaCheck";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "UC -Early Text Description";
									- Stereotypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IHandle 
											- _m2Class = "IStereotype";
											- _filename = "PredefinedTypes.sbs";
											- _subsystem = "PredefinedTypes";
											- _class = "";
											- _name = "Query";
											- _id = GUID 4c77a3b1-822f-466e-bd06-76145c9e3b88;
										}
									}
									- _modifiedTimeWeak = 6.9.2014::17:11:56;
									- Tags = { IRPYRawContainer 
										- size = 4;
										- value = 
										{ ITag 
											- _id = GUID 1b71e034-b08b-4c87-a16f-3d3cb5de54f5;
											- _myState = 8192;
											- _name = "Tag_Name";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 2721f085-ddfa-44a8-b637-9f8f7ce4d942;
													- _modifiedTimeWeak = 6.9.2014::17:8:12;
													- _value = "Maturity";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Name";
												- _id = GUID 3358798e-bfb4-426b-a12d-552274ee65e5;
											}
										}
										{ ITag 
											- _id = GUID d49b8b5d-b9a4-4cf9-8429-b8b7fde953cd;
											- _myState = 8192;
											- _name = "Tag_Value";
											- _modifiedTimeWeak = 6.9.2014::17:11:56;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 1a63f114-76a3-44a1-acf4-58204b1bf6d8;
													- _modifiedTimeWeak = 6.9.2014::17:11:56;
													- _value = "Early Text Description";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Value";
												- _id = GUID 41c58abd-ed56-47c6-80e0-88ce9852cd43;
											}
										}
										{ ITag 
											- _id = GUID 41ffa939-3bab-4f8f-a6a8-c6a0f0b64d3b;
											- _myState = 8192;
											- _name = "Conform_Viewpoint";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID e0c244c1-fb0a-42ce-868f-fc6eec48defb;
											- _myState = 8192;
											- _name = "Or_And_Veiwpoint";
											- _modifiedTimeWeak = 6.9.2014::17:11:56;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 6be6fe39-f016-4d73-8bb7-7610a27d1037;
													- _modifiedTimeWeak = 6.9.2014::17:11:56;
													- _value = "or";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 399e5f15-af07-4539-b24a-c5d3e13a1ecb;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
								}
								{ ITableLayout 
									- _id = GUID 399e5f15-af07-4539-b24a-c5d3e13a1ecb;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 1;
															- value = 
															{ IProperty 
																- _Name = "EnableCriteriaCheck";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "UC - Evolving Description";
									- Stereotypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IHandle 
											- _m2Class = "IStereotype";
											- _filename = "PredefinedTypes.sbs";
											- _subsystem = "PredefinedTypes";
											- _class = "";
											- _name = "Query";
											- _id = GUID 4c77a3b1-822f-466e-bd06-76145c9e3b88;
										}
									}
									- _modifiedTimeWeak = 6.9.2014::17:10:54;
									- Tags = { IRPYRawContainer 
										- size = 4;
										- value = 
										{ ITag 
											- _id = GUID 700b4623-6c4e-4391-b40e-788310d927a1;
											- _myState = 8192;
											- _name = "Tag_Name";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID f59e2b07-3e08-4f0d-ba9f-e9b18e26ee0b;
													- _modifiedTimeWeak = 6.9.2014::17:8:12;
													- _value = "Maturity";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Name";
												- _id = GUID 3358798e-bfb4-426b-a12d-552274ee65e5;
											}
										}
										{ ITag 
											- _id = GUID cb448759-d88a-4888-905a-c16a46663cef;
											- _myState = 8192;
											- _name = "Tag_Value";
											- _modifiedTimeWeak = 6.9.2014::17:10:54;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 0a966d19-f019-42e6-b8cf-7ef8c2ee3aeb;
													- _modifiedTimeWeak = 6.9.2014::17:10:54;
													- _value = "Evolving Description";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Value";
												- _id = GUID 41c58abd-ed56-47c6-80e0-88ce9852cd43;
											}
										}
										{ ITag 
											- _id = GUID 2e3bbf44-7993-476d-ab40-869d490fe6a0;
											- _myState = 8192;
											- _name = "Conform_Viewpoint";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID 1d89dc01-694a-4879-b8b7-95b2c2c74b56;
											- _myState = 8192;
											- _name = "Or_And_Veiwpoint";
											- _modifiedTimeWeak = 6.9.2014::17:10:54;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID f8bef777-82af-4846-be19-0a83cf95b2ab;
													- _modifiedTimeWeak = 6.9.2014::17:10:54;
													- _value = "or";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 399e5f15-af07-4539-b24a-c5d3e13a1ecb;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
								}
								{ ITableLayout 
									- _id = GUID fb0bfc59-6c0f-4401-bb9c-f7108e9d0b71;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 1;
															- value = 
															{ IProperty 
																- _Name = "EnableCriteriaCheck";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "UC - Description Reviewed";
									- Stereotypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IHandle 
											- _m2Class = "IStereotype";
											- _filename = "PredefinedTypes.sbs";
											- _subsystem = "PredefinedTypes";
											- _class = "";
											- _name = "Query";
											- _id = GUID 4c77a3b1-822f-466e-bd06-76145c9e3b88;
										}
									}
									- _modifiedTimeWeak = 6.9.2014::17:13:34;
									- Tags = { IRPYRawContainer 
										- size = 4;
										- value = 
										{ ITag 
											- _id = GUID 54ce6419-6231-425b-9b19-31ecdc52e482;
											- _myState = 8192;
											- _name = "Tag_Name";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 3800ce93-60e7-4ca2-8d79-2a10b2014fcc;
													- _modifiedTimeWeak = 6.9.2014::17:8:12;
													- _value = "Maturity";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Name";
												- _id = GUID 3358798e-bfb4-426b-a12d-552274ee65e5;
											}
										}
										{ ITag 
											- _id = GUID 1c486a05-086d-4720-920f-7f1924ff0fa3;
											- _myState = 8192;
											- _name = "Tag_Value";
											- _modifiedTimeWeak = 6.9.2014::17:13:34;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID d0cdba6a-0392-454a-bb41-e627acd01d2d;
													- _modifiedTimeWeak = 6.9.2014::17:13:34;
													- _value = "Description Reviewed";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Value";
												- _id = GUID 41c58abd-ed56-47c6-80e0-88ce9852cd43;
											}
										}
										{ ITag 
											- _id = GUID 46fc8fdf-62ba-41f7-927f-fd556bc30523;
											- _myState = 8192;
											- _name = "Conform_Viewpoint";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID 24921dfb-fcb9-4c6d-bf8b-4ec2a8d94b06;
											- _myState = 8192;
											- _name = "Or_And_Veiwpoint";
											- _modifiedTimeWeak = 6.9.2014::17:13:34;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID b6d337df-f58f-4dae-9423-1eb22141fc80;
													- _modifiedTimeWeak = 6.9.2014::17:13:34;
													- _value = "or";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 399e5f15-af07-4539-b24a-c5d3e13a1ecb;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
								}
								{ ITableLayout 
									- _id = GUID a7b7c326-6f55-48b0-90f3-124b45d35301;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 1;
															- value = 
															{ IProperty 
																- _Name = "EnableCriteriaCheck";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "UC - Early Activity";
									- Stereotypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IHandle 
											- _m2Class = "IStereotype";
											- _filename = "PredefinedTypes.sbs";
											- _subsystem = "PredefinedTypes";
											- _class = "";
											- _name = "Query";
											- _id = GUID 4c77a3b1-822f-466e-bd06-76145c9e3b88;
										}
									}
									- _modifiedTimeWeak = 6.9.2014::17:14:2;
									- Tags = { IRPYRawContainer 
										- size = 4;
										- value = 
										{ ITag 
											- _id = GUID 5c968911-0b7a-4610-a6bd-d4fa77ea1086;
											- _myState = 8192;
											- _name = "Tag_Name";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID d9908757-c21b-4cc8-8df7-1b8908355273;
													- _modifiedTimeWeak = 6.9.2014::17:8:12;
													- _value = "Maturity";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Name";
												- _id = GUID 3358798e-bfb4-426b-a12d-552274ee65e5;
											}
										}
										{ ITag 
											- _id = GUID 20cc5223-6ecd-4ff4-8d5c-1107446a2ab0;
											- _myState = 8192;
											- _name = "Tag_Value";
											- _modifiedTimeWeak = 6.9.2014::17:14:2;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID d1982023-33b4-4fb4-a569-54e5c54efdd4;
													- _modifiedTimeWeak = 6.9.2014::17:14:2;
													- _value = "Early Activity";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Value";
												- _id = GUID 41c58abd-ed56-47c6-80e0-88ce9852cd43;
											}
										}
										{ ITag 
											- _id = GUID e75b9def-3f2e-411f-8205-c8521a83f1ce;
											- _myState = 8192;
											- _name = "Conform_Viewpoint";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID 842c1b97-3f1b-487a-9033-ce0e5d816f68;
											- _myState = 8192;
											- _name = "Or_And_Veiwpoint";
											- _modifiedTimeWeak = 6.9.2014::17:14:2;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 722b8d55-0ba6-4879-a3e2-385f67c399cc;
													- _modifiedTimeWeak = 6.9.2014::17:14:2;
													- _value = "or";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 399e5f15-af07-4539-b24a-c5d3e13a1ecb;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
								}
								{ ITableLayout 
									- _id = GUID f05ebfd0-60a4-45e1-9af7-52c148a77bda;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 1;
															- value = 
															{ IProperty 
																- _Name = "EnableCriteriaCheck";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "UC - Evolving Activity";
									- Stereotypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IHandle 
											- _m2Class = "IStereotype";
											- _filename = "PredefinedTypes.sbs";
											- _subsystem = "PredefinedTypes";
											- _class = "";
											- _name = "Query";
											- _id = GUID 4c77a3b1-822f-466e-bd06-76145c9e3b88;
										}
									}
									- _modifiedTimeWeak = 6.9.2014::17:14:47;
									- Tags = { IRPYRawContainer 
										- size = 4;
										- value = 
										{ ITag 
											- _id = GUID 7d1b5689-43e4-44da-bff1-17e0266a4fd6;
											- _myState = 8192;
											- _name = "Tag_Name";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID e312fa4d-91bb-48f6-9a28-a7c4d5516bff;
													- _modifiedTimeWeak = 6.9.2014::17:8:12;
													- _value = "Maturity";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Name";
												- _id = GUID 3358798e-bfb4-426b-a12d-552274ee65e5;
											}
										}
										{ ITag 
											- _id = GUID 878ee6e6-be4a-4d6e-9361-ec85992912e1;
											- _myState = 8192;
											- _name = "Tag_Value";
											- _modifiedTimeWeak = 6.9.2014::17:14:47;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 8a254cd3-1389-406c-8f96-6c5e66af8b73;
													- _modifiedTimeWeak = 6.9.2014::17:14:47;
													- _value = "Evolving Activity";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Value";
												- _id = GUID 41c58abd-ed56-47c6-80e0-88ce9852cd43;
											}
										}
										{ ITag 
											- _id = GUID e13ab641-15d5-4e4c-8fee-396debe24e96;
											- _myState = 8192;
											- _name = "Conform_Viewpoint";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID e3fe3ab9-7961-49b8-8edc-9d82613c9c30;
											- _myState = 8192;
											- _name = "Or_And_Veiwpoint";
											- _modifiedTimeWeak = 6.9.2014::17:14:47;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID f4e42a25-c811-4d8d-b9ce-e753c9608983;
													- _modifiedTimeWeak = 6.9.2014::17:14:47;
													- _value = "or";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 399e5f15-af07-4539-b24a-c5d3e13a1ecb;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
								}
								{ ITableLayout 
									- _id = GUID 56077a4f-2001-49fd-89f6-9216891aaaf3;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 1;
															- value = 
															{ IProperty 
																- _Name = "EnableCriteriaCheck";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "UC - Activity Complete";
									- Stereotypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IHandle 
											- _m2Class = "IStereotype";
											- _filename = "PredefinedTypes.sbs";
											- _subsystem = "PredefinedTypes";
											- _class = "";
											- _name = "Query";
											- _id = GUID 4c77a3b1-822f-466e-bd06-76145c9e3b88;
										}
									}
									- _modifiedTimeWeak = 6.9.2014::17:15:4;
									- Tags = { IRPYRawContainer 
										- size = 4;
										- value = 
										{ ITag 
											- _id = GUID 3e4a27e0-8918-40ff-8c91-1bbe06ba2c55;
											- _myState = 8192;
											- _name = "Tag_Name";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 79c590d1-f1a2-4f21-b98f-7f3d4ed110f5;
													- _modifiedTimeWeak = 6.9.2014::17:8:12;
													- _value = "Maturity";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Name";
												- _id = GUID 3358798e-bfb4-426b-a12d-552274ee65e5;
											}
										}
										{ ITag 
											- _id = GUID 62d6112d-cf15-40b7-9fa3-a8e847185e0b;
											- _myState = 8192;
											- _name = "Tag_Value";
											- _modifiedTimeWeak = 6.9.2014::17:15:4;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 2c87401a-6606-425f-be4d-b0a05d5e3286;
													- _modifiedTimeWeak = 6.9.2014::17:15:4;
													- _value = "Activity Complete";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Tag_Value";
												- _id = GUID 41c58abd-ed56-47c6-80e0-88ce9852cd43;
											}
										}
										{ ITag 
											- _id = GUID c1ead1e2-38fb-4972-a002-d95d158787c1;
											- _myState = 8192;
											- _name = "Conform_Viewpoint";
											- _modifiedTimeWeak = 6.9.2014::17:8:12;
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID deb4c9e5-2c05-4c2b-86da-43e38b114fed;
											- _myState = 8192;
											- _name = "Or_And_Veiwpoint";
											- _modifiedTimeWeak = 6.9.2014::17:15:4;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID a6e380d5-f4b5-47eb-b994-497997aa58b7;
													- _modifiedTimeWeak = 6.9.2014::17:15:4;
													- _value = "or";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 399e5f15-af07-4539-b24a-c5d3e13a1ecb;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
								}
								{ ITableLayout 
									- _id = GUID c7baf13d-9f17-4421-9857-97e393742ccc;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 1;
															- value = 
															{ IProperty 
																- _Name = "CollapseFirstColumn";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "Use Case List";
									- _modifiedTimeWeak = 4.10.2015::18:50:47;
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0de9637a-ba26-43f4-9159-5beb301e6c29;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
									- DataColumns = { IRPYRawContainer 
										- size = 2;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID c7baf13d-9f17-4421-9857-97e393742ccc;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Owner";
											- _columnName = "Use Case Category";
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID c7baf13d-9f17-4421-9857-97e393742ccc;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Name";
											- _columnName = "Use Case Name";
										}
									}
								}
								{ ITableLayout 
									- _id = GUID cd684a08-e615-4a6e-99f2-39b250208cd0;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 2;
															- value = 
															{ IProperty 
																- _Name = "CollapseFirstColumn";
																- _Value = "False";
																- _Type = Bool;
															}
															{ IProperty 
																- _Name = "EnableCriteriaCheck";
																- _Value = "True";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "Workflow Pattern Activities Layout";
									- _modifiedTimeWeak = 9.22.2015::19:24:11;
									- Tags = { IRPYRawContainer 
										- size = 6;
										- value = 
										{ ITag 
											- _id = GUID 40b00ff9-66ea-44da-ba7b-53d6e4bd5c4f;
											- _myState = 8192;
											- _name = "Conform_Viewpoint";
											- _modifiedTimeWeak = 2.5.2014::14:42:54;
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID b99d1ef8-f6d7-46a3-a0f2-3336d8a1dbbb;
											- _myState = 8192;
											- _name = "Or_And_Veiwpoint";
											- _modifiedTimeWeak = 9.23.2014::1:19:40;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 9c7585a6-4b6f-4dbc-b501-b759689fca4e;
													- _modifiedTimeWeak = 9.23.2014::1:19:40;
													- _value = "or";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID 11acf337-13d3-4f37-968f-82d39a92c960;
											- _myState = 8192;
											- _name = "Search_User_Code";
											- _modifiedTimeWeak = 9.23.2014::1:19:40;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 244368e1-0e59-431d-97ad-248e67eaa6ee;
													- _modifiedTimeWeak = 9.23.2014::1:19:40;
													- _value = "False";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpBoolean";
												- _id = GUID f19b56f2-78ab-44fa-860e-6ead487ecb07;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Search_User_Code";
												- _id = GUID 83589a2d-ccae-4b66-bd8f-f2b7be717861;
											}
										}
										{ ITag 
											- _id = GUID c1cc8eb5-8caf-42d6-9930-804d615f4f44;
											- _myState = 8192;
											- _name = "Search_Other_Text";
											- _modifiedTimeWeak = 9.23.2014::1:19:40;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID a678845b-5cbe-4c01-b829-03c439f3ee9d;
													- _modifiedTimeWeak = 9.23.2014::1:19:40;
													- _value = "False";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpBoolean";
												- _id = GUID f19b56f2-78ab-44fa-860e-6ead487ecb07;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Search_Other_Text";
												- _id = GUID 30a8af2c-8397-4393-a7d7-dd8db888d8da;
											}
										}
										{ ITag 
											- _id = GUID 38ac5a96-b299-4995-b326-918f15a7d4e0;
											- _myState = 8192;
											- _name = "Search_Element_Name";
											- _modifiedTimeWeak = 9.23.2014::1:19:40;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID 12aadf95-ee89-4283-946b-b0cc1d6dff7a;
													- _modifiedTimeWeak = 9.23.2014::1:19:40;
													- _value = "False";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpBoolean";
												- _id = GUID f19b56f2-78ab-44fa-860e-6ead487ecb07;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Search_Element_Name";
												- _id = GUID 58af4c27-0694-4e04-ab8a-62b491b053ea;
											}
										}
										{ ITag 
											- _id = GUID 29221d81-acab-4791-86ef-de3fe6b54e99;
											- _myState = 8192;
											- _name = "Stereotype_Requirement";
											- _modifiedTimeWeak = 9.23.2014::1:19:40;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IInstanceValue 
													- _id = GUID 33a70bce-b49d-484f-8eea-c561b71215e6;
													- _modifiedTimeWeak = 1.2.1990::0:0:0;
													- _value = { IHandle 
														- _m2Class = "IStereotype";
														- _filename = "SE_Dev_Profile.sbs";
														- _subsystem = "SE_Dev_Profile";
														- _class = "";
														- _name = "WkFlPattern";
														- _id = GUID 85802e88-a0e2-448b-b8b4-050f4cb0ec94;
													}
												}
											}
											- myTypeOf = { IType 
												- _id = GUID d1ddbe4b-c988-4250-aa19-2cfe8da4a627;
												- _myState = 8192;
												- _modifiedTimeWeak = 1.2.1990::0:0:0;
												- _declaration = "Stereotype";
												- _kind = Language;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Stereotype_Requirement";
												- _id = GUID a249681c-22f5-4a25-b372-3cf2758f1473;
											}
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 2;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID cd684a08-e615-4a6e-99f2-39b250208cd0;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "ActivityDiagram";
											- _DataType = 2;
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID cd684a08-e615-4a6e-99f2-39b250208cd0;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
									- DataColumns = { IRPYRawContainer 
										- size = 2;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID cd684a08-e615-4a6e-99f2-39b250208cd0;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Name";
											- _columnName = "Use Case";
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID cd684a08-e615-4a6e-99f2-39b250208cd0;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Owner";
											- _columnName = "Owning Elements";
										}
									}
									- TableFromElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "Actor";
											- _DataType = 2;
										}
									}
									- TableToElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
								}
								{ ITableLayout 
									- _id = GUID b506a3d1-5646-41bb-b8c3-3bb37eac2729;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 1;
															- value = 
															{ IProperty 
																- _Name = "EnableCriteriaCheck";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "WorkFlowPatternQuery";
									- Stereotypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IHandle 
											- _m2Class = "IStereotype";
											- _filename = "PredefinedTypes.sbs";
											- _subsystem = "PredefinedTypes";
											- _class = "";
											- _name = "Query";
											- _id = GUID 4c77a3b1-822f-466e-bd06-76145c9e3b88;
										}
									}
									- _modifiedTimeWeak = 9.23.2014::1:32:6;
									- Tags = { IRPYRawContainer 
										- size = 3;
										- value = 
										{ ITag 
											- _id = GUID b2a94e35-62e0-4395-b0c6-3878232c4961;
											- _myState = 8192;
											- _name = "Conform_Viewpoint";
											- _modifiedTimeWeak = 9.23.2014::1:17:47;
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID 92172446-cbf6-425a-9dcb-2c0f6a805e1f;
											- _myState = 8192;
											- _name = "Or_And_Veiwpoint";
											- _modifiedTimeWeak = 9.23.2014::1:32:6;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID e0802d2c-fb95-411b-8378-2dc770bb34e2;
													- _modifiedTimeWeak = 9.23.2014::1:32:6;
													- _value = "or";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID b6821e53-f308-4cf9-ab50-777dd0b8b201;
											- _myState = 8192;
											- _name = "Stereotype_Requirement";
											- _modifiedTimeWeak = 9.23.2014::1:32:6;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ IInstanceValue 
													- _id = GUID e9e243c5-b96a-473c-add2-21295aaa5778;
													- _modifiedTimeWeak = 1.2.1990::0:0:0;
													- _value = { IHandle 
														- _m2Class = "IStereotype";
														- _filename = "SE_Dev_Profile.sbs";
														- _subsystem = "SE_Dev_Profile";
														- _class = "";
														- _name = "WkFlPattern";
														- _id = GUID 85802e88-a0e2-448b-b8b4-050f4cb0ec94;
													}
												}
											}
											- myTypeOf = { IType 
												- _id = GUID f95b06d9-b5b6-4803-8a66-1bf1a0671ab4;
												- _myState = 8192;
												- _modifiedTimeWeak = 1.2.1990::0:0:0;
												- _declaration = "Stereotype";
												- _kind = Language;
											}
											- _isOrdered = 0;
											- _base = { IHandle 
												- _m2Class = "ITag";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "Query";
												- _name = "Stereotype_Requirement";
												- _id = GUID a249681c-22f5-4a25-b372-3cf2758f1473;
											}
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID b506a3d1-5646-41bb-b8c3-3bb37eac2729;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "ActivityDiagram";
											- _DataType = 2;
										}
									}
								}
								{ ITableLayout 
									- _id = GUID 5e4dfa1e-8675-4c2c-a8e9-524ff4ef883e;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 1;
															- value = 
															{ IProperty 
																- _Name = "CollapseFirstColumn";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "Available Activities Table Layout";
									- _modifiedTimeWeak = 4.6.2015::19:15:10;
									- _description = { IDescription 
										- _text = "Provides a list of all activities within the model with their parend and their location.";
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 5e4dfa1e-8675-4c2c-a8e9-524ff4ef883e;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "ActivityDiagram";
											- _DataType = 2;
										}
									}
									- DataColumns = { IRPYRawContainer 
										- size = 3;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 5e4dfa1e-8675-4c2c-a8e9-524ff4ef883e;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Name";
											- _columnName = "Name";
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 5e4dfa1e-8675-4c2c-a8e9-524ff4ef883e;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Owner";
											- _columnName = "Owner";
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 5e4dfa1e-8675-4c2c-a8e9-524ff4ef883e;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Full path name";
											- _columnName = "Full path name";
										}
									}
								}
								{ ITableLayout 
									- _id = GUID 0ee4f918-f71c-4f12-a6fd-bd5822d0ac62;
									- _myState = 8192;
									- _properties = { IPropertyContainer 
										- Subjects = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertySubject 
												- _Name = "Model";
												- Metaclasses = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IPropertyMetaclass 
														- _Name = "TableLayout";
														- Properties = { IRPYRawContainer 
															- size = 2;
															- value = 
															{ IProperty 
																- _Name = "CollapseFirstColumn";
																- _Value = "False";
																- _Type = Bool;
															}
															{ IProperty 
																- _Name = "EnableCriteriaCheck";
																- _Value = "False";
																- _Type = Bool;
															}
														}
													}
												}
											}
										}
									}
									- _name = "Use Cases Description Layout";
									- _modifiedTimeWeak = 7.24.2015::14:47:2;
									- Tags = { IRPYRawContainer 
										- size = 2;
										- value = 
										{ ITag 
											- _id = GUID a42ee042-99a0-4a8c-980f-c473c5b4520c;
											- _myState = 8192;
											- _name = "Conform_Viewpoint";
											- _modifiedTimeWeak = 2.5.2014::14:42:54;
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
										{ ITag 
											- _id = GUID 293b67a1-5dc2-49d8-8171-8eb1520937b7;
											- _myState = 8192;
											- _name = "Or_And_Veiwpoint";
											- _modifiedTimeWeak = 2.5.2014::14:43:10;
											- ValueSpecifications = { IRPYRawContainer 
												- size = 1;
												- value = 
												{ ILiteralSpecification 
													- _id = GUID b19be92a-965c-4d8b-8d3a-4210f99dec53;
													- _modifiedTimeWeak = 2.5.2014::14:43:10;
													- _value = "or";
												}
											}
											- _typeOf = { IHandle 
												- _m2Class = "IType";
												- _filename = "PredefinedTypes.sbs";
												- _subsystem = "PredefinedTypes";
												- _class = "";
												- _name = "RhpString";
												- _id = GUID ae5e3720-4e3e-40f1-9346-9a8b4e501f35;
											}
											- _isOrdered = 0;
										}
									}
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 1b7fef36-dd14-49fa-909c-2a358af3a2a2;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
									- DataColumns = { IRPYRawContainer 
										- size = 2;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0ee4f918-f71c-4f12-a6fd-bd5822d0ac62;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Name";
											- _columnName = "Use Case";
										}
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0ee4f918-f71c-4f12-a6fd-bd5822d0ac62;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "General.Description";
											- _columnName = "Description";
										}
									}
									- TableFromElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "Actor";
											- _DataType = 2;
										}
									}
									- TableToElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
								}
								{ ITableLayout 
									- _id = GUID b37edbeb-f2e8-4e59-8b34-e0f82efce15e;
									- _myState = 8192;
									- _name = "Total Use Cases";
									- Stereotypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ IHandle 
											- _m2Class = "IStereotype";
											- _filename = "PredefinedTypes.sbs";
											- _subsystem = "PredefinedTypes";
											- _class = "";
											- _name = "Query";
											- _id = GUID 4c77a3b1-822f-466e-bd06-76145c9e3b88;
										}
									}
									- _modifiedTimeWeak = 9.22.2015::19:35:4;
									- TableElementTypes = { IRPYRawContainer 
										- size = 1;
										- value = 
										{ TableDataDefinition 
											- _myTable = { IHandle 
												- _m2Class = "ITableLayout";
												- _id = GUID b37edbeb-f2e8-4e59-8b34-e0f82efce15e;
											}
											- _modelElement = { IHandle 
												- _m2Class = "";
											}
											- _name = "UseCase";
											- _DataType = 2;
										}
									}
								}
							}
							- _configurationRelatedTime = 1.2.1990::0:0:0;
						}
					}
					- weakCGTime = 12.14.2015::15:21:10;
					- strongCGTime = 3.29.2015::15:52:25;
					- _defaultComposite = GUID 57acf9df-3d8f-404d-889f-d6f81f515dc3;
					- _eventsBaseID = -1;
					- Classes = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IClass 
							- _id = GUID 57acf9df-3d8f-404d-889f-d6f81f515dc3;
							- _myState = 40960;
							- _name = "TopLevel";
							- _modifiedTimeWeak = 3.29.2015::15:52:25;
							- weakCGTime = 3.29.2015::15:52:25;
							- strongCGTime = 3.29.2015::15:52:25;
							- _multiplicity = "";
							- _itsStateChart = { IHandle 
								- _m2Class = "";
							}
							- _classModifier = Unspecified;
						}
					}
					- TableInstances = { IRPYRawContainer 
						- size = 9;
						- value = 
						{ ITableInstance 
							- _id = GUID ac55221f-bcba-4ef7-bc03-4693d26534da;
							- _myState = 8192;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "TableView";
												- Properties = { IRPYRawContainer 
													- size = 2;
													- value = 
													{ IProperty 
														- _Name = "TableFilters";
														- _Value = "";
														- _Type = String;
													}
													{ IProperty 
														- _Name = "TableSortColumnState";
														- _Value = "1,0,0";
														- _Type = String;
													}
												}
											}
										}
									}
								}
							}
							- _name = "Use Case Description and Stage Table View";
							- _modifiedTimeWeak = 9.22.2015::19:13:23;
							- LayoutHandle = { IHandle 
								- _m2Class = "ITableLayout";
								- _id = GUID 1b7fef36-dd14-49fa-909c-2a358af3a2a2;
							}
							- ScopeHandles = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IHandle 
									- _m2Class = "ISubsystem";
									- _id = GUID 6bca94b1-3700-4982-9b60-2821c4b41793;
								}
							}
						}
						{ ITableInstance 
							- _id = GUID 5befc027-2b9b-442f-bc74-35a2500268ca;
							- _myState = 8192;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "TableView";
												- Properties = { IRPYRawContainer 
													- size = 2;
													- value = 
													{ IProperty 
														- _Name = "TableFilters";
														- _Value = "Priority,,High,,TRUE,,FALSE,,FALSE,,FALSE,,FALSE,,FALSE,,FALSE";
														- _Type = String;
													}
													{ IProperty 
														- _Name = "TableSortColumnState";
														- _Value = "1,1,-1,0";
														- _Type = String;
													}
												}
											}
										}
									}
								}
							}
							- _name = "Use Case Priority and Maturity Table View";
							- _modifiedTimeWeak = 12.14.2015::15:21:10;
							- LayoutHandle = { IHandle 
								- _m2Class = "ITableLayout";
								- _id = GUID 0de9637a-ba26-43f4-9159-5beb301e6c29;
							}
							- ScopeHandles = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IHandle 
									- _m2Class = "ISubsystem";
									- _id = GUID 6bca94b1-3700-4982-9b60-2821c4b41793;
								}
							}
						}
						{ ITableInstance 
							- _id = GUID 40f15fe2-2ce9-4f13-b19a-fe8fdf37caf7;
							- _myState = 8192;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "TableView";
												- Properties = { IRPYRawContainer 
													- size = 2;
													- value = 
													{ IProperty 
														- _Name = "TableFilters";
														- _Value = "";
														- _Type = String;
													}
													{ IProperty 
														- _Name = "TableSortColumnState";
														- _Value = "1,0,0";
														- _Type = String;
													}
												}
											}
										}
									}
								}
							}
							- _name = "Use Case and Actor Table View";
							- _modifiedTimeWeak = 11.17.2014::14:9:14;
							- LayoutHandle = { IHandle 
								- _m2Class = "ITableLayout";
								- _id = GUID 0270a1e5-520d-4288-9667-0c52e589ce2d;
							}
							- ScopeHandles = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IHandle 
									- _m2Class = "ISubsystem";
									- _id = GUID 6bca94b1-3700-4982-9b60-2821c4b41793;
								}
							}
						}
						{ ITableInstance 
							- _id = GUID 05046cb8-9474-4c9d-8470-5492fe70dcd3;
							- _myState = 8192;
							- _name = "Use Case Maturity";
							- Stereotypes = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IHandle 
									- _m2Class = "IStereotype";
									- _filename = "PredefinedTypes.sbs";
									- _subsystem = "PredefinedTypes";
									- _class = "";
									- _name = "MetricsView";
									- _id = GUID 852d68e8-b380-45fd-a997-66cc2aaf9289;
								}
							}
							- _modifiedTimeWeak = 9.22.2015::19:32:57;
							- LayoutHandle = { IHandle 
								- _m2Class = "ITableLayout";
								- _id = GUID 8d318d1b-111e-4a8e-9a9c-4f30e723aca8;
							}
							- ScopeHandles = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IHandle 
									- _m2Class = "ISubsystem";
									- _id = GUID 6bca94b1-3700-4982-9b60-2821c4b41793;
								}
							}
						}
						{ ITableInstance 
							- _id = GUID a3370548-e995-4f3e-a5ca-ae4bda450fed;
							- _myState = 8192;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "TableView";
												- Properties = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IProperty 
														- _Name = "TableSortColumnState";
														- _Value = "1,0";
														- _Type = String;
													}
												}
											}
										}
									}
								}
							}
							- _name = "Use Case List View";
							- _modifiedTimeWeak = 7.26.2015::13:40:37;
							- LayoutHandle = { IHandle 
								- _m2Class = "ITableLayout";
								- _id = GUID c7baf13d-9f17-4421-9857-97e393742ccc;
							}
							- ScopeHandles = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IHandle 
									- _m2Class = "ISubsystem";
									- _id = GUID 6bca94b1-3700-4982-9b60-2821c4b41793;
								}
							}
						}
						{ ITableInstance 
							- _id = GUID 826497fb-245b-41a5-b863-a085eefb86c5;
							- _myState = 8192;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "TableView";
												- Properties = { IRPYRawContainer 
													- size = 2;
													- value = 
													{ IProperty 
														- _Name = "TableFilters";
														- _Value = "Stage,,Domain,,TRUE,,FALSE,,FALSE,,FALSE,,FALSE,,FALSE,,FALSE";
														- _Type = String;
													}
													{ IProperty 
														- _Name = "TableSortColumnState";
														- _Value = "1,0,0";
														- _Type = String;
													}
												}
											}
										}
									}
								}
							}
							- _name = "Workflow Pattern Activities View";
							- _modifiedTimeWeak = 9.22.2015::22:58:0;
							- LayoutHandle = { IHandle 
								- _m2Class = "ITableLayout";
								- _id = GUID cd684a08-e615-4a6e-99f2-39b250208cd0;
							}
							- ScopeHandles = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IHandle 
									- _m2Class = "";
								}
							}
						}
						{ ITableInstance 
							- _id = GUID 120c3ddc-baa5-49ef-a293-7d5b2adfb477;
							- _myState = 8192;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "TableView";
												- Properties = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IProperty 
														- _Name = "TableSortColumnState";
														- _Value = "1,0,0";
														- _Type = String;
													}
												}
											}
										}
									}
								}
							}
							- _name = "All Available Activities Table View";
							- _modifiedTimeWeak = 9.22.2015::19:9:51;
							- LayoutHandle = { IHandle 
								- _m2Class = "ITableLayout";
								- _id = GUID 5e4dfa1e-8675-4c2c-a8e9-524ff4ef883e;
							}
							- ScopeHandles = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IHandle 
									- _m2Class = "IProject";
									- _id = GUID d84478ea-c8fb-444f-aecc-3acdf582da60;
								}
							}
						}
						{ ITableInstance 
							- _id = GUID af755c5f-785d-4a42-8f36-7dc91fab2272;
							- _myState = 8192;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "TableView";
												- Properties = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IProperty 
														- _Name = "TableSortColumnState";
														- _Value = "1,0,0";
														- _Type = String;
													}
												}
											}
										}
									}
								}
							}
							- _name = "Available Activities in SE Ops Table View";
							- _modifiedTimeWeak = 4.29.2015::21:43:2;
							- LayoutHandle = { IHandle 
								- _m2Class = "ITableLayout";
								- _id = GUID 5e4dfa1e-8675-4c2c-a8e9-524ff4ef883e;
							}
							- ScopeHandles = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IHandle 
									- _m2Class = "";
								}
							}
						}
						{ ITableInstance 
							- _id = GUID 2a817ce6-118c-46f1-98c8-57e4d7c7f5dc;
							- _myState = 8192;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "TableView";
												- Properties = { IRPYRawContainer 
													- size = 2;
													- value = 
													{ IProperty 
														- _Name = "TableFilters";
														- _Value = "";
														- _Type = String;
													}
													{ IProperty 
														- _Name = "TableSortColumnState";
														- _Value = "1,0,0";
														- _Type = String;
													}
												}
											}
										}
									}
								}
							}
							- _name = "Use Case Description Table View";
							- _modifiedTimeWeak = 7.24.2015::14:46:41;
							- LayoutHandle = { IHandle 
								- _m2Class = "ITableLayout";
								- _id = GUID 0ee4f918-f71c-4f12-a6fd-bd5822d0ac62;
							}
							- ScopeHandles = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IHandle 
									- _m2Class = "ISubsystem";
									- _id = GUID 6bca94b1-3700-4982-9b60-2821c4b41793;
								}
							}
						}
					}
					- _configurationRelatedTime = 1.2.1990::0:0:0;
				}
				{ ISubsystem 
					- fileName = "Actors";
					- _id = GUID d3fbc632-ba58-461c-8443-17a96c04ed6e;
				}
				{ ISubsystem 
					- fileName = "Exploratory_and_Concept_Stage";
					- _id = GUID 5d69c9d4-3a32-49fc-829e-51b39c74246d;
					- _name = "Exploratory and Concept Stage";
				}
				{ ISubsystem 
					- fileName = "System_Development_Stage";
					- _id = GUID 1cac8b15-93af-4e74-8c1e-6da70b8dc4d1;
					- _name = "System Development Stage";
				}
				{ ISubsystem 
					- fileName = "Production_Stage";
					- _id = GUID e8e5671e-b495-4d41-a575-df3971b040cf;
					- _name = "Production Stage";
				}
				{ ISubsystem 
					- fileName = "Product_and_Service_Life_Management_Stage";
					- _id = GUID 6a02d8c1-5bc8-481c-af89-a42c05be3ac5;
					- _name = "Product and Service Life Management Stage";
				}
				{ IDiagram 
					- _id = GUID 5eb2f333-93d6-437c-aabe-47136547f99d;
					- _myState = 8192;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Comment";
										- Properties = { IRPYRawContainer 
											- size = 7;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,116,60";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Tahoma";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Size@Child.NameCompartment@Stereotype";
												- _Value = "6";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "194,192,192";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
									{ IPropertyMetaclass 
										- _Name = "ContainArrow";
										- Properties = { IRPYRawContainer 
											- size = 4;
											- value = 
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Tahoma";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "128,128,128";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
									{ IPropertyMetaclass 
										- _Name = "Depends";
										- Properties = { IRPYRawContainer 
											- size = 5;
											- value = 
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Tahoma";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "128,128,128";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "2";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "0";
												- _Type = Int;
											}
										}
									}
									{ IPropertyMetaclass 
										- _Name = "DiagramFrame";
										- Properties = { IRPYRawContainer 
											- size = 8;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "20,20,590,500";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "247,247,247";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Fill.Transparent_Fill";
												- _Value = "0";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Tahoma";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "700";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "194,192,192";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
									{ IPropertyMetaclass 
										- _Name = "Package";
										- Properties = { IRPYRawContainer 
											- size = 7;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,216,151";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Tahoma";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Weight@Child.NameCompartment@Name";
												- _Value = "700";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "109,163,217";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
									{ IPropertyMetaclass 
										- _Name = "problem";
										- Properties = { IRPYRawContainer 
											- size = 7;
											- value = 
											{ IProperty 
												- _Name = "DefaultSize";
												- _Value = "0,0,116,60";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "255,255,255";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Font.Font";
												- _Value = "Tahoma";
												- _Type = String;
											}
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "8";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Font.Size@Child.NameCompartment@Stereotype";
												- _Value = "6";
												- _Type = Int;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "194,192,192";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineWidth";
												- _Value = "1";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- _name = "Lifecycle Use Case Organization";
					- Stereotypes = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IStereotype";
							- _filename = "$OMROOT\\Profiles\\SysML\\SysMLProfile_rpy\\SysML.sbs";
							- _subsystem = "SysML::Diagrams";
							- _class = "";
							- _name = "Package Diagram";
							- _id = GUID 240f8214-239e-4ada-91e6-f49f2497f4d9;
						}
					}
					- _modifiedTimeWeak = 1.2.1990::0:0:0;
					- _lastModifiedTime = "12.2.2015::13:6:48";
					- _graphicChart = { CGIClassChart 
						- _id = GUID 5fa92e41-f767-4fe4-817c-a9b877ad2321;
						- m_type = 0;
						- m_pModelObject = { IHandle 
							- _m2Class = "IDiagram";
							- _id = GUID 5eb2f333-93d6-437c-aabe-47136547f99d;
						}
						- m_pParent = ;
						- m_name = { CGIText 
							- m_str = "";
							- m_style = "Arial" 10 0 0 0 1 ;
							- m_color = { IColor 
								- m_fgColor = 0;
								- m_bgColor = 0;
								- m_bgFlag = 0;
							}
							- m_position = 1 0 0  ;
							- m_nIdent = 0;
							- m_bImplicitSetRectPoints = 0;
							- m_nOrientationCtrlPt = 8;
						}
						- m_drawBehavior = 0;
						- m_bIsPreferencesInitialized = 0;
						- elementList = 15;
						{ CGIClass 
							- _id = GUID 2ab0b1a5-9cc8-45ea-9e71-15fe69664f1b;
							- m_type = 78;
							- m_pModelObject = { IHandle 
								- _m2Class = "IClass";
								- _id = GUID 096ed2a3-f9af-4729-b836-e0906b514d83;
							}
							- m_pParent = ;
							- m_name = { CGIText 
								- m_str = "TopLevel";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 5;
							}
							- m_drawBehavior = 0;
							- m_bIsPreferencesInitialized = 0;
							- m_AdditionalLabel = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 1;
							}
							- m_polygon = 0 ;
							- m_nNameFormat = 0;
							- m_nIsNameFormat = 0;
							- Compartments = { IRPYRawContainer 
								- size = 2;
								- value = 
								{ CGICompartment 
									- _id = GUID 8766a127-d8b4-4009-900f-cb964a57f491;
									- m_name = "Attribute";
									- m_displayOption = Explicit;
									- m_bShowInherited = 0;
									- m_bOrdered = 0;
									- Items = { IRPYRawContainer 
										- size = 0;
									}
								}
								{ CGICompartment 
									- _id = GUID f56cae63-31b9-4613-8d1f-89be547bfcc8;
									- m_name = "Operation";
									- m_displayOption = Explicit;
									- m_bShowInherited = 0;
									- m_bOrdered = 0;
									- Items = { IRPYRawContainer 
										- size = 0;
									}
								}
							}
							- Attrs = { IRPYRawContainer 
								- size = 0;
							}
							- Operations = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGIDiagramFrame 
							- _id = GUID abc12545-488c-4564-a241-7cc7d493f561;
							- m_type = 203;
							- m_pModelObject = { IHandle 
								- _m2Class = "";
							}
							- m_pParent = GUID 2ab0b1a5-9cc8-45ea-9e71-15fe69664f1b;
							- m_name = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 8;
							}
							- m_drawBehavior = 4096;
							- m_transform = 3.62037 0 0 4.65152 8 20 ;
							- m_bIsPreferencesInitialized = 1;
							- m_AdditionalLabel = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 1;
							}
							- m_polygon = 4 0 0  0 132  216 132  216 0  ;
							- m_nNameFormat = 0;
							- m_nIsNameFormat = 0;
							- Compartments = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGIPackage 
							- _id = GUID c69279ad-de06-47ef-bb76-7e8980ace080;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "Graphics";
												- Properties = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IProperty 
														- _Name = "FitBoxToItsTextuals";
														- _Value = "False";
														- _Type = Bool;
													}
												}
											}
										}
									}
								}
							}
							- m_type = 127;
							- m_pModelObject = { IHandle 
								- _m2Class = "ISubsystem";
								- _id = GUID c469f8a5-924d-4311-8ccb-368e28548a19;
							}
							- m_pParent = GUID 26365f2f-587f-41ec-bd43-8170e079aaa0;
							- m_name = { CGIText 
								- m_str = "SE Life Cycle Workflow Use Cases::Use Case Table Views";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 5;
							}
							- m_drawBehavior = 1032;
							- m_transform = 0.375368 0 0 0.157894 78.8914 42.4693 ;
							- m_bIsPreferencesInitialized = 1;
							- m_AdditionalLabel = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 1;
							}
							- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
							- m_nNameFormat = 0;
							- m_nIsNameFormat = 0;
							- Compartments = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGIPackage 
							- _id = GUID 8a72d5f5-9982-4a00-9f3d-f4244ff0cc4f;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "Graphics";
												- Properties = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IProperty 
														- _Name = "FitBoxToItsTextuals";
														- _Value = "False";
														- _Type = Bool;
													}
												}
											}
										}
									}
								}
							}
							- m_type = 127;
							- m_pModelObject = { IHandle 
								- _m2Class = "ISubsystem";
								- _filename = "Actors.sbs";
								- _subsystem = "SE Life Cycle Workflow Use Cases";
								- _class = "";
								- _name = "Actors";
								- _id = GUID d3fbc632-ba58-461c-8443-17a96c04ed6e;
							}
							- m_pParent = GUID 26365f2f-587f-41ec-bd43-8170e079aaa0;
							- m_name = { CGIText 
								- m_str = "Actors";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 5;
							}
							- m_drawBehavior = 4104;
							- m_transform = 0.292682 0 0 0.108772 543.739 97.1329 ;
							- m_bIsPreferencesInitialized = 1;
							- m_AdditionalLabel = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 1;
							}
							- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
							- m_nNameFormat = 0;
							- m_nIsNameFormat = 0;
							- Compartments = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGIPackage 
							- _id = GUID a3a914c1-ffe3-49e4-ab57-ad6be7737452;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "Graphics";
												- Properties = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IProperty 
														- _Name = "FitBoxToItsTextuals";
														- _Value = "False";
														- _Type = Bool;
													}
												}
											}
										}
									}
								}
							}
							- m_type = 127;
							- m_pModelObject = { IHandle 
								- _m2Class = "ISubsystem";
								- _filename = "Exploratory_and_Concept_Stage.sbs";
								- _subsystem = "SE Life Cycle Workflow Use Cases";
								- _class = "";
								- _name = "Exploratory and Concept Stage";
								- _id = GUID 5d69c9d4-3a32-49fc-829e-51b39c74246d;
							}
							- m_pParent = GUID 26365f2f-587f-41ec-bd43-8170e079aaa0;
							- m_name = { CGIText 
								- m_str = "Exploratory and Concept Stage";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 5;
							}
							- m_drawBehavior = 4104;
							- m_transform = 0.414971 0 0 0.126316 254.363 286.192 ;
							- m_bIsPreferencesInitialized = 1;
							- m_AdditionalLabel = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 1;
							}
							- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
							- m_nNameFormat = 0;
							- m_nIsNameFormat = 0;
							- Compartments = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGIPackage 
							- _id = GUID 9f7bafc6-4ef1-4256-a45d-dab075d7298f;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "Graphics";
												- Properties = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IProperty 
														- _Name = "FitBoxToItsTextuals";
														- _Value = "False";
														- _Type = Bool;
													}
												}
											}
										}
									}
								}
							}
							- m_type = 127;
							- m_pModelObject = { IHandle 
								- _m2Class = "ISubsystem";
								- _filename = "System_Development_Stage.sbs";
								- _subsystem = "SE Life Cycle Workflow Use Cases";
								- _class = "";
								- _name = "System Development Stage";
								- _id = GUID 1cac8b15-93af-4e74-8c1e-6da70b8dc4d1;
							}
							- m_pParent = GUID 26365f2f-587f-41ec-bd43-8170e079aaa0;
							- m_name = { CGIText 
								- m_str = "System Development Stage";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 5;
							}
							- m_drawBehavior = 4104;
							- m_transform = 0.415988 0 0 0.0998755 247.154 471.247 ;
							- m_bIsPreferencesInitialized = 1;
							- m_AdditionalLabel = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 1;
							}
							- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
							- m_nNameFormat = 0;
							- m_nIsNameFormat = 0;
							- Compartments = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGIPackage 
							- _id = GUID 8b257f2b-64d4-4c20-b5a0-07cfc8df3688;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "Graphics";
												- Properties = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IProperty 
														- _Name = "FitBoxToItsTextuals";
														- _Value = "False";
														- _Type = Bool;
													}
												}
											}
										}
									}
								}
							}
							- m_type = 127;
							- m_pModelObject = { IHandle 
								- _m2Class = "ISubsystem";
								- _filename = "Production_Stage.sbs";
								- _subsystem = "SE Life Cycle Workflow Use Cases";
								- _class = "";
								- _name = "Production Stage";
								- _id = GUID e8e5671e-b495-4d41-a575-df3971b040cf;
							}
							- m_pParent = GUID 26365f2f-587f-41ec-bd43-8170e079aaa0;
							- m_name = { CGIText 
								- m_str = "Production Stage";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 5;
							}
							- m_drawBehavior = 4104;
							- m_transform = 0.415988 0 0 0.0982455 243.858 832.813 ;
							- m_bIsPreferencesInitialized = 1;
							- m_AdditionalLabel = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 1;
							}
							- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
							- m_nNameFormat = 0;
							- m_nIsNameFormat = 0;
							- Compartments = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGIPackage 
							- _id = GUID e7e603b6-0624-42fa-978f-bfc0e0274bc7;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "Graphics";
												- Properties = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IProperty 
														- _Name = "FitBoxToItsTextuals";
														- _Value = "False";
														- _Type = Bool;
													}
												}
											}
										}
									}
								}
							}
							- m_type = 127;
							- m_pModelObject = { IHandle 
								- _m2Class = "ISubsystem";
								- _filename = "Product_and_Service_Life_Management_Stage.sbs";
								- _subsystem = "SE Life Cycle Workflow Use Cases";
								- _class = "";
								- _name = "Product and Service Life Management Stage";
								- _id = GUID 6a02d8c1-5bc8-481c-af89-a42c05be3ac5;
							}
							- m_pParent = GUID 26365f2f-587f-41ec-bd43-8170e079aaa0;
							- m_name = { CGIText 
								- m_str = "Product and Service Life Management Stage";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 5;
							}
							- m_drawBehavior = 4104;
							- m_transform = 0.415988 0 0 0.121937 237.267 984.873 ;
							- m_bIsPreferencesInitialized = 1;
							- m_AdditionalLabel = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 1;
							}
							- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
							- m_nNameFormat = 0;
							- m_nIsNameFormat = 0;
							- Compartments = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGIPackage 
							- _id = GUID 26365f2f-587f-41ec-bd43-8170e079aaa0;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "Graphics";
												- Properties = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IProperty 
														- _Name = "FitBoxToItsTextuals";
														- _Value = "False";
														- _Type = Bool;
													}
												}
											}
										}
									}
								}
							}
							- m_type = 127;
							- m_pModelObject = { IHandle 
								- _m2Class = "ISubsystem";
								- _id = GUID 6bca94b1-3700-4982-9b60-2821c4b41793;
							}
							- m_pParent = GUID 2ab0b1a5-9cc8-45ea-9e71-15fe69664f1b;
							- m_name = { CGIText 
								- m_str = "SE Life Cycle Workflow Use Cases";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 5;
							}
							- m_drawBehavior = 4104;
							- m_transform = 0.626646 0 0 0.49522 18 54.0534 ;
							- m_bIsPreferencesInitialized = 1;
							- m_AdditionalLabel = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 1;
							}
							- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
							- m_nNameFormat = 0;
							- m_nIsNameFormat = 0;
							- Compartments = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGIPackage 
							- _id = GUID faeec2fc-0798-44d5-babd-c986013e1b04;
							- m_type = 127;
							- m_pModelObject = { IHandle 
								- _m2Class = "ISubsystem";
								- _filename = "Management_Workflow_Use_Cases.sbs";
								- _subsystem = "SE Life Cycle Workflow Use Cases::System Development Stage";
								- _class = "";
								- _name = "Management Workflow Use Cases";
								- _id = GUID 9c9eecbf-70ef-447f-bcb2-895c6548c211;
							}
							- m_pParent = GUID 26365f2f-587f-41ec-bd43-8170e079aaa0;
							- m_name = { CGIText 
								- m_str = "Management Workflow Use Cases";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 5;
							}
							- m_drawBehavior = 4104;
							- m_transform = 0.292682 0 0 0.094737 19.7723 680.397 ;
							- m_bIsPreferencesInitialized = 1;
							- m_AdditionalLabel = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 1;
							}
							- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
							- m_nNameFormat = 0;
							- m_nIsNameFormat = 0;
							- Compartments = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGIPackage 
							- _id = GUID 6d8d6fd7-fb4e-4f05-9b20-16910e3e793a;
							- m_type = 127;
							- m_pModelObject = { IHandle 
								- _m2Class = "ISubsystem";
								- _filename = "SE_Domain_Workflow_Use_Cases.sbs";
								- _subsystem = "SE Life Cycle Workflow Use Cases::System Development Stage";
								- _class = "";
								- _name = "SE Domain Workflow Use Cases";
								- _id = GUID 81c5a56b-9b7c-4c90-97ad-f11f8d46ddf9;
							}
							- m_pParent = GUID 26365f2f-587f-41ec-bd43-8170e079aaa0;
							- m_name = { CGIText 
								- m_str = "SE Domain Workflow Use Cases";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 5;
							}
							- m_drawBehavior = 4104;
							- m_transform = 0.292682 0 0 0.094737 415.219 680.397 ;
							- m_bIsPreferencesInitialized = 1;
							- m_AdditionalLabel = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 1;
							}
							- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
							- m_nNameFormat = 0;
							- m_nIsNameFormat = 0;
							- Compartments = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGIPackage 
							- _id = GUID b11f915f-d32c-4a80-8b4f-6a8735a28766;
							- _properties = { IPropertyContainer 
								- Subjects = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertySubject 
										- _Name = "General";
										- Metaclasses = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IPropertyMetaclass 
												- _Name = "Graphics";
												- Properties = { IRPYRawContainer 
													- size = 1;
													- value = 
													{ IProperty 
														- _Name = "FitBoxToItsTextuals";
														- _Value = "False";
														- _Type = Bool;
													}
												}
											}
										}
									}
								}
							}
							- m_type = 127;
							- m_pModelObject = { IHandle 
								- _m2Class = "ISubsystem";
								- _filename = "Validation_and_Verification_Workflow_Use_Cases.sbs";
								- _subsystem = "SE Life Cycle Workflow Use Cases::System Development Stage";
								- _class = "";
								- _name = "Validation and Verification Workflow Use Cases";
								- _id = GUID d50621e9-6d94-4e96-a575-8d3ee5c2e7f0;
							}
							- m_pParent = GUID 26365f2f-587f-41ec-bd43-8170e079aaa0;
							- m_name = { CGIText 
								- m_str = "Validation and Verification Workflow Use Cases";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 5;
							}
							- m_drawBehavior = 4104;
							- m_transform = 0.330708 0 0 0.094737 804.282 678.378 ;
							- m_bIsPreferencesInitialized = 1;
							- m_AdditionalLabel = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 1;
							}
							- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
							- m_nNameFormat = 0;
							- m_nIsNameFormat = 0;
							- Compartments = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGIContainArrow 
							- _id = GUID faa50ef9-25e4-4b2c-9d1b-29a7f1345b1a;
							- m_type = 204;
							- m_pModelObject = { IHandle 
								- _m2Class = "";
							}
							- m_pParent = ;
							- m_name = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 8;
							}
							- m_drawBehavior = 4096;
							- m_bIsPreferencesInitialized = 1;
							- m_pSource = GUID faeec2fc-0798-44d5-babd-c986013e1b04;
							- m_sourceType = 'F';
							- m_pTarget = GUID 9f7bafc6-4ef1-4256-a45d-dab075d7298f;
							- m_targetType = 'T';
							- m_direction = ' ';
							- m_rpn = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 8;
							}
							- m_arrow = 2 92 365  328 365  ;
							- m_anglePoint1 = 0 0 ;
							- m_anglePoint2 = 0 0 ;
							- m_line_style = 2;
							- m_SourcePort = 338 149 ;
							- m_TargetPort = 594 861 ;
						}
						{ CGIContainArrow 
							- _id = GUID bdb7c181-c41e-49ba-a24d-a4485457cb9c;
							- m_type = 204;
							- m_pModelObject = { IHandle 
								- _m2Class = "";
							}
							- m_pParent = ;
							- m_name = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 8;
							}
							- m_drawBehavior = 4096;
							- m_bIsPreferencesInitialized = 1;
							- m_pSource = GUID 6d8d6fd7-fb4e-4f05-9b20-16910e3e793a;
							- m_sourceType = 'F';
							- m_pTarget = GUID 9f7bafc6-4ef1-4256-a45d-dab075d7298f;
							- m_targetType = 'T';
							- m_direction = ' ';
							- m_rpn = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 8;
							}
							- m_anglePoint1 = 0 0 ;
							- m_anglePoint2 = 0 0 ;
							- m_line_style = 2;
							- m_SourcePort = 270 618 ;
							- m_TargetPort = 594 578 ;
						}
						{ CGIContainArrow 
							- _id = GUID 08bc1451-eaae-47ff-887c-d8adb5c30bd1;
							- m_type = 204;
							- m_pModelObject = { IHandle 
								- _m2Class = "";
							}
							- m_pParent = ;
							- m_name = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 8;
							}
							- m_drawBehavior = 4096;
							- m_bIsPreferencesInitialized = 1;
							- m_pSource = GUID b11f915f-d32c-4a80-8b4f-6a8735a28766;
							- m_sourceType = 'F';
							- m_pTarget = GUID 9f7bafc6-4ef1-4256-a45d-dab075d7298f;
							- m_targetType = 'T';
							- m_direction = ' ';
							- m_rpn = { CGIText 
								- m_str = "";
								- m_style = "Arial" 10 0 0 0 1 ;
								- m_color = { IColor 
									- m_fgColor = 0;
									- m_bgColor = 0;
									- m_bgFlag = 0;
								}
								- m_position = 1 0 0  ;
								- m_nIdent = 0;
								- m_bImplicitSetRectPoints = 0;
								- m_nOrientationCtrlPt = 8;
							}
							- m_arrow = 2 576 365  330 365  ;
							- m_anglePoint1 = 0 0 ;
							- m_anglePoint2 = 0 0 ;
							- m_line_style = 2;
							- m_SourcePort = 261 0 ;
							- m_TargetPort = 603 1103 ;
						}
						
						- m_access = 'Z';
						- m_modified = 'N';
						- m_fileVersion = "";
						- m_nModifyDate = 0;
						- m_nCreateDate = 0;
						- m_creator = "";
						- m_bScaleWithZoom = 1;
						- m_arrowStyle = 'S';
						- m_pRoot = GUID 2ab0b1a5-9cc8-45ea-9e71-15fe69664f1b;
						- m_currentLeftTop = 0 0 ;
						- m_currentRightBottom = 0 0 ;
					}
					- _defaultSubsystem = { IHandle 
						- _m2Class = "ISubsystem";
						- _id = GUID 6bca94b1-3700-4982-9b60-2821c4b41793;
					}
				}
				{ ISubsystem 
					- fileName = "Worflow_Patterns";
					- _id = GUID c27fc8c5-127d-4141-8990-da58e0eda24b;
					- _name = "Worflow Patterns";
				}
			}
			- weakCGTime = 12.14.2015::15:21:10;
			- strongCGTime = 11.11.2015::17:0:58;
			- _defaultComposite = GUID 096ed2a3-f9af-4729-b836-e0906b514d83;
			- _eventsBaseID = -1;
			- Classes = { IRPYRawContainer 
				- size = 1;
				- value = 
				{ IClass 
					- _id = GUID 096ed2a3-f9af-4729-b836-e0906b514d83;
					- _myState = 40960;
					- _name = "TopLevel";
					- _modifiedTimeWeak = 3.29.2015::15:52:25;
					- weakCGTime = 3.29.2015::15:52:25;
					- strongCGTime = 3.29.2015::15:52:25;
					- _multiplicity = "";
					- _itsStateChart = { IHandle 
						- _m2Class = "";
					}
					- _classModifier = Unspecified;
				}
			}
			- _configurationRelatedTime = 3.7.2014::17:58:22;
		}
		{ ISubsystem 
			- fileName = "Information_Model";
			- _id = GUID 303e4fc1-00d6-4fe5-a49b-1820cffd395f;
			- _name = "Information Model";
		}
		{ ISubsystem 
			- fileName = "Generated_Documents";
			- _persistAs = "Generated_Documents";
			- _id = GUID ec647722-1ed8-4c1e-add4-60795884cdaa;
			- _name = "Generated Documents";
		}
		{ ISubsystem 
			- fileName = "Playground_Temp";
			- _id = GUID e14f70a9-2bf9-4c79-a5e7-7eccacc7251b;
			- _name = "Playground Temp";
		}
		{ ISubsystem 
			- fileName = "Imported_Library";
			- _persistAs = "Imported_Library";
			- _id = GUID b7fb2034-0c0e-42bd-bc42-62da3ac643b6;
			- _name = "Imported__Libraries";
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre805Cpp";
			- _id = GUID a32649f4-8029-4846-82f3-6deba65e416d;
		}
		{ IProfile 
			- fileName = "ExtendedTableCapabilities";
			- _persistAs = "$OMROOT\\Profiles\\MicroC";
			- _id = GUID 305908cd-5da2-4b10-8ba9-bcff3246b79a;
			- _isReference = 1;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre81Cpp";
			- _id = GUID dcd2cdb5-4c74-4d47-99ca-1b358b271e5f;
		}
		{ IProfile 
			- fileName = "ModelBasedDocumentGeneration";
			- _persistAs = "$OMROOT\\Profiles\\ModelBasedDocumentGeneration";
			- _id = GUID 7b488349-0f81-419c-9a89-cfdfc5b3cff5;
			- _isReference = 1;
		}
		{ IProfile 
			- fileName = "ExportImport";
			- _persistAs = "$SCRIPTROOT\\ExportImport";
			- _id = GUID 2d884707-2787-40bd-b7e2-e74c48aa8db8;
			- _isReference = 1;
		}
		{ IProfile 
			- fileName = "Technical_Measures_Library_and_Profile";
			- _persistAs = "..\\..\\..\\..\\..\\Documents\\SystemModeling\\RhapsodyAdd-ins\\TechnicalMeasures\\TMProfileAndLibraryForRhapsody811AndAbove";
			- _id = GUID 70f16c1c-0b77-4c59-b16e-eadff6e6d475;
			- _name = "Technical Measures Library and Profile";
			- _isReference = 1;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre812Cpp";
			- _id = GUID 3026d3ea-02b4-49ae-b086-6982c27412f0;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre813Cpp";
			- _id = GUID 803c9619-7509-44c3-bfdf-6fee2352ab55;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 0;
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID bfdb8f53-2bc6-49d2-8bed-99a758995a97;
		}
	}
}

