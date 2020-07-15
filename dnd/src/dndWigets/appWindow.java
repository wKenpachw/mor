package dndWigets;

import org.eclipse.swt.SWT;
import org.eclipse.swt.layout.RowData;
import org.eclipse.swt.layout.RowLayout;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Label;
import org.eclipse.swt.widgets.List;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Composite;
import org.eclipse.swt.layout.GridData;
import org.eclipse.swt.widgets.Menu;
import org.eclipse.swt.widgets.MenuItem;
import org.eclipse.swt.widgets.TabFolder;
import org.eclipse.swt.widgets.TabItem;
import org.eclipse.swt.widgets.Table;

import java.util.ArrayList;

import org.eclipse.jface.viewers.ArrayContentProvider;
import org.eclipse.jface.viewers.CellEditor;
import org.eclipse.jface.viewers.ColumnLabelProvider;
import org.eclipse.jface.viewers.IBaseLabelProvider;
import org.eclipse.jface.viewers.ICellModifier;
import org.eclipse.jface.viewers.IContentProvider;
import org.eclipse.jface.viewers.ILabelProviderListener;
import org.eclipse.jface.viewers.TableViewer;
import org.eclipse.swt.widgets.TableColumn;

import dndCharacter.CharInfo;
import dndLogic.CharLabelProvider;

import org.eclipse.jface.viewers.TableViewerColumn;
import org.eclipse.jface.viewers.TextCellEditor;
import org.eclipse.jface.viewers.Viewer;
import org.eclipse.jface.viewers.ViewerComparator;
import org.eclipse.jface.viewers.ViewerSorter;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.custom.ScrolledComposite;
import org.eclipse.swt.events.SelectionEvent;
import org.eclipse.swt.events.SelectionListener;
import org.eclipse.wb.swt.SWTResourceManager;

public class appWindow {
	public static Table charTable;
	public static Display display = new Display();
	public static Shell shell = new Shell(display);

	public static TableViewer charTableViewer;
	public static Button addButton;
	public static Button dellButton;
	public static Button copyButton;

	public static void main(String[] args) {

		widgets();
		table();

		shell.open();
		while (!shell.isDisposed()) {
			if (!display.readAndDispatch())
				display.sleep();
		}
		display.dispose();
	}

	public static void widgets() {
		shell.setText("Morozov's dungeons");
		shell.setSize(826, 672);
		shell.setLayout(new GridLayout(1, false));

		Menu menu = new Menu(shell, SWT.BAR);
		shell.setMenuBar(menu);

		MenuItem mntmNewSubmenu = new MenuItem(menu, SWT.CASCADE);
		mntmNewSubmenu.setText("New SubMenu");

		Menu menu_1 = new Menu(mntmNewSubmenu);
		mntmNewSubmenu.setMenu(menu_1);

		MenuItem mntmNewItem = new MenuItem(menu_1, SWT.NONE);
		mntmNewItem.setText("New Item");

		TabFolder tabFolder = new TabFolder(shell, SWT.NONE);
		tabFolder.setLayoutData(new GridData(SWT.FILL, SWT.FILL, true, true, 1, 1));

		TabItem charTabItem = new TabItem(tabFolder, SWT.NONE);
		charTabItem.setText("\u041F\u0435\u0440\u0441\u043E\u043D\u0430\u0436\u0438");

		Composite charComposite = new Composite(tabFolder, SWT.NONE);
		charTabItem.setControl(charComposite);
		charComposite.setLayout(new GridLayout(2, false));

		charTableViewer = new TableViewer(charComposite, SWT.BORDER | SWT.FULL_SELECTION | SWT.HIDE_SELECTION);
		charTable = charTableViewer.getTable();
		charTable.setFont(SWTResourceManager.getFont("Segoe UI", 9, SWT.NORMAL));
		charTable.setLinesVisible(true);
		charTable.setHeaderVisible(true);
		charTable.setLayoutData(new GridData(SWT.FILL, SWT.FILL, true, true, 1, 1));
		charTableViewer.setComparator(new ViewerComparator() {

			public int compare(Viewer viewer, Object e1, Object e2) {

				CharInfo char1 = (CharInfo) e1;
				CharInfo char2 = (CharInfo) e2;
				int init1 = char1.getInit();
				int init2 = char2.getInit();
				System.out.println(init1);
				System.out.println(init2);
				if (init1 > init2)
					return -1;
				else if (init1 < init2)
					return 1;

				return 1;
			}
		});

		TableViewerColumn nameTableViewerColumn = new TableViewerColumn(charTableViewer, SWT.NONE);
		TableColumn nameColumn = nameTableViewerColumn.getColumn();
		nameColumn.setWidth(160);
		nameColumn.setText("\u0418\u043C\u044F");

		TableViewerColumn initTableViewerColumn = new TableViewerColumn(charTableViewer, SWT.NONE);
		TableColumn initColumn = initTableViewerColumn.getColumn();
		initColumn.setWidth(119);
		initColumn.setText("\u0418\u043D\u0438\u0446\u0438\u0430\u0442\u0438\u0432\u0430");
//		initTableViewerColumn.getViewer().setComparator(new ViewerComparator() {
//			@Override
//			public int compare(Viewer viewer, Object e1, Object e2) {
//				// TODO Auto-generated method stub
//				return 1;
////				return super.compare(viewer, e1, e2);
//			}
//		});

		TableViewerColumn maxHPTableViewerColumn_3 = new TableViewerColumn(charTableViewer, SWT.NONE);
		TableColumn maxHpColumn = maxHPTableViewerColumn_3.getColumn();
		maxHpColumn.setWidth(174);
		maxHpColumn.setText(
				"\u041C\u0430\u043A\u0441\u0438\u043C\u0430\u043B\u044C\u043D\u044B\u0435 \u0436\u0438\u0437\u043D\u0438");

		TableViewerColumn currentHPtableViewerColumn = new TableViewerColumn(charTableViewer, SWT.NONE);
		TableColumn currentHPColumn = currentHPtableViewerColumn.getColumn();
		currentHPColumn.setWidth(140);
		currentHPColumn.setText("\u0422\u0435\u043A\u0443\u0449\u0438\u0435 \u0436\u0438\u0437\u043D\u0438");

		Composite tableButtonsComposite = new Composite(charComposite, SWT.BORDER);
		tableButtonsComposite.setLayout(new GridLayout(1, false));
		tableButtonsComposite.setLayoutData(new GridData(SWT.FILL, SWT.FILL, false, true, 1, 1));

		addButton = new Button(tableButtonsComposite, SWT.NONE);
		addButton.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, false, false, 1, 1));
		addButton.setText("\u0414\u043E\u0431\u0430\u0432\u0438\u0442\u044C");

		dellButton = new Button(tableButtonsComposite, SWT.NONE);
		dellButton.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, false, false, 1, 1));
		dellButton.setText("\u0423\u0434\u0430\u043B\u0438\u0442\u044C");

		copyButton = new Button(tableButtonsComposite, SWT.NONE);
		copyButton.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, false, false, 1, 1));
		copyButton.setText("\u041A\u043E\u043F\u0438\u0440\u043E\u0432\u0430\u0442\u044C");

		Button pasteNewButton = new Button(tableButtonsComposite, SWT.NONE);
		pasteNewButton.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, false, false, 1, 1));
		pasteNewButton.setText("\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044C");
		pasteNewButton.addSelectionListener(new SelectionListener() {
			
			@Override
			public void widgetSelected(SelectionEvent arg0) {
				CharInfo[] ob = (CharInfo[]) charTableViewer.getInput();
				charTableViewer.setInput(ob);
			}
			
			@Override
			public void widgetDefaultSelected(SelectionEvent arg0) {
				// TODO Auto-generated method stub
				
			}
		});

		Composite dopInfoComposite = new Composite(charComposite, SWT.BORDER);
		dopInfoComposite.setLayoutData(new GridData(SWT.FILL, SWT.FILL, true, true, 2, 1));

		TabItem musicTabItem = new TabItem(tabFolder, SWT.NONE);
		musicTabItem.setText("\u041C\u0443\u0437\u044B\u043A\u0430");

		Composite composite_3 = new Composite(tabFolder, SWT.NONE);
		musicTabItem.setControl(composite_3);
		composite_3.setLayout(new GridLayout(1, false));

		TabItem documentsTabItem = new TabItem(tabFolder, SWT.NONE);
		documentsTabItem.setText("\u0414\u043E\u043A\u0443\u043C\u0435\u043D\u0442\u044B");

		Composite composite = new Composite(tabFolder, SWT.NONE);
		documentsTabItem.setControl(composite);
		composite.setLayout(new GridLayout(2, false));

		ScrolledComposite scrolledComposite = new ScrolledComposite(composite,
				SWT.BORDER | SWT.H_SCROLL | SWT.V_SCROLL);
		scrolledComposite.setLayoutData(new GridData(SWT.FILL, SWT.FILL, true, true, 1, 1));
		scrolledComposite.setExpandHorizontal(true);
		scrolledComposite.setExpandVertical(true);

		TabFolder tabFolder_1 = new TabFolder(scrolledComposite, SWT.NONE);
		scrolledComposite.setContent(tabFolder_1);
		scrolledComposite.setMinSize(tabFolder_1.computeSize(SWT.DEFAULT, SWT.DEFAULT));

		Composite composite_1 = new Composite(composite, SWT.NONE);
		composite_1.setLayout(new GridLayout(1, false));
		composite_1.setLayoutData(new GridData(SWT.FILL, SWT.FILL, false, true, 1, 1));

		Button btnNewButton = new Button(composite_1, SWT.NONE);
		btnNewButton.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, true, false, 1, 1));
		btnNewButton.setText("\u041E\u0442\u043A\u0440\u044B\u0442\u044C...");

		Button button = new Button(composite_1, SWT.NONE);
		button.setText("\u0414\u0443\u0431\u043B\u0438\u0440\u043E\u0432\u0430\u0442\u044C");

		Button button_1 = new Button(composite_1, SWT.NONE);
		button_1.setLayoutData(new GridData(SWT.FILL, SWT.CENTER, false, false, 1, 1));
		button_1.setText("\u0417\u0430\u043A\u0440\u044B\u0442\u044C");

	}

	public static void table() {

		charTableViewer.setContentProvider(new ArrayContentProvider());
		charTableViewer.setLabelProvider(new CharLabelProvider());
		charTableViewer.setColumnProperties(new String[] { "Имя", "Инициатива", "Максимальное ХП", "Текущее ХП" });
		CellEditor[] editors = new CellEditor[4];
		editors[0] = new TextCellEditor(charTable);
		editors[1] = new TextCellEditor(charTable);
		editors[2] = new TextCellEditor(charTable);
		editors[3] = new TextCellEditor(charTable);
		charTableViewer.setCellEditors(editors);

		charTableViewer.setCellModifier(new ICellModifier() {

			@Override
			public void modify(Object arg0, String arg1, Object arg2) {

				CharInfo charInfo = (CharInfo) charTableViewer.getStructuredSelection().getFirstElement();
				try {
					switch (arg1) {
					case "Имя": {
						System.out.println("name1");
						charInfo.setName(arg2.toString());
						break;
					}
					case "Инициатива": {
						System.out.println("init1");
						charInfo.setInit(Integer.valueOf(arg2.toString()));
						break;
					}
					case "Текущее ХП": {
						System.out.println("cur1");
						int val = Integer.valueOf(arg2.toString());
						int cur = charInfo.getCurrentHP();
						charInfo.setCurrenHP(charInfo.getCurrentHP() - val);
						break;
					}
					case "Максимальное ХП": {
						System.out.println("max1");
						int cur = charInfo.getCurrentHP();
						charInfo.setMaxHP(Integer.valueOf(arg2.toString()));
						if (cur == 0)
							charInfo.setCurrenHP(charInfo.getMaxHP());
						break;
					}

					}
					charTableViewer.refresh(charInfo);
				} catch (Exception e) {
					System.out.println("Введено не корректное значение");
				}
			}

			@Override
			public Object getValue(Object arg0, String arg1) {
				CharInfo charInfo = (CharInfo) arg0;

				switch (arg1) {
				case "Имя": {
					return charInfo.getName();
				}
				case "Инициатива": {
					return String.valueOf(charInfo.getInit());
				}
				case "Текущие ХП": {
					return String.valueOf(charInfo.getCurrentHP());
				}
				case "Максимальное ХП": {
					return String.valueOf(charInfo.getMaxHP());
				}

				}
				return "";
			}

			@Override
			public boolean canModify(Object arg0, String arg1) {
				return true;
			}
		});

		addButton.addSelectionListener(new SelectionListener() {

			@Override
			public void widgetSelected(SelectionEvent arg0) {
				ArrayList <CharInfo> mass = new ArrayList<CharInfo>();
				
				System.out.println(charTableViewer.getInput().toString());
//				for (CharInfo inf: (CharInfo[]) charTableViewer.getInput()) {
//					mass.add(inf);
//				}
//				charTableViewer.add(new CharInfo("", 1, 1, 1, ""));
				mass.add(new CharInfo("", 1, 1, 1, ""));
				charTableViewer.setInput(mass);
//				charTableViewer.refresh();
			}

			@Override
			public void widgetDefaultSelected(SelectionEvent arg0) {
			}
		});

		dellButton.addSelectionListener(new SelectionListener() {

			@Override
			public void widgetSelected(SelectionEvent arg0) {
				try {
					charTableViewer.remove(charTableViewer.getStructuredSelection().getFirstElement());
				} catch (Exception e) {
					System.out.println("Необходимо выбрать строку");
				}
			}

			@Override
			public void widgetDefaultSelected(SelectionEvent arg0) {
				// TODO Auto-generated method stub

			}
		});
		copyButton.addSelectionListener(new SelectionListener() {

			@Override
			public void widgetSelected(SelectionEvent arg0) {
				CharInfo ch = (CharInfo) charTableViewer.getStructuredSelection().getFirstElement();
				charTableViewer
						.add(new CharInfo(ch.getName(), ch.getInit(), ch.getMaxHP(), ch.getMaxHP(), ch.getDopInfo()));

			}

			@Override
			public void widgetDefaultSelected(SelectionEvent arg0) {
				// TODO Auto-generated method stub

			}
		});

	}
}
