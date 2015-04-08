I-Logix-RPY-Archive version 8.10.0 C++ 6930133
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
								- _Value = "C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD.EXE";
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
					{ IPropertyMetaclass 
						- _Name = "block";
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
	- _modifiedTimeWeak = 4.8.2015::18:2:32;
	- _lastID = 31;
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
			- _count = 3;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = 3;
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
		- size = 18;
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
			- fileName = "System_Engineering_Operations";
			- _id = GUID 6cfa223b-3cca-4a39-932e-465247fcef40;
			- _name = "System Engineering Operations";
		}
		{ ISubsystem 
			- fileName = "Information_Model";
			- _id = GUID 303e4fc1-00d6-4fe5-a49b-1820cffd395f;
			- _name = "Information Model";
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
		{ ISubsystem 
			- _id = GUID af2b6f5f-c94a-45b7-a689-95ca444007a0;
			- _myState = 8192;
			- _name = "Temp";
			- _modifiedTimeWeak = 2.23.2015::12:24:46;
			- weakCGTime = 2.23.2015::12:24:46;
			- strongCGTime = 2.23.2015::12:24:46;
			- _defaultComposite = GUID 76911e3c-4590-470f-904e-31a8cdca6c54;
			- _eventsBaseID = -1;
			- Classes = { IRPYRawContainer 
				- size = 1;
				- value = 
				{ IClass 
					- _id = GUID 76911e3c-4590-470f-904e-31a8cdca6c54;
					- _myState = 40960;
					- _name = "TopLevel";
					- _modifiedTimeWeak = 1.2.1990::0:0:0;
					- weakCGTime = 1.2.1990::0:0:0;
					- strongCGTime = 1.2.1990::0:0:0;
					- _multiplicity = "";
					- _itsStateChart = { IHandle 
						- _m2Class = "";
					}
					- _classModifier = Unspecified;
				}
			}
			- _configurationRelatedTime = 1.2.1990::0:0:0;
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

